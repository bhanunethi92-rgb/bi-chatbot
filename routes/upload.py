from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io
from services.data_service import generate_summary

router = APIRouter()

data_store = {}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.csv', '.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Only CSV/Excel files allowed")

    contents = await file.read()

    try:
        if file.filename.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(contents))
        else:
            df = pd.read_excel(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not parse file: {str(e)}")

    data_store["df"] = df
    data_store["filename"] = file.filename
    data_store["summary"] = generate_summary(df)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "rows": len(df),
        "columns": list(df.columns),
        "preview": df.head(5).to_dict(orient="records"),
        "summary": data_store["summary"]
    }

@router.get("/data-info")
def get_data_info():
    if "df" not in data_store:
        raise HTTPException(status_code=404, detail="No file uploaded yet")
    df = data_store["df"]
    return {
        "filename": data_store["filename"],
        "rows": len(df),
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "preview": df.head(5).to_dict(orient="records"),
        "summary": data_store["summary"]
    }

def get_data_store():
    return data_store
