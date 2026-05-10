import pandas as pd

def generate_summary(df: pd.DataFrame) -> str:
    summary = []

    summary.append(f"Dataset has {len(df)} rows and {len(df.columns)} columns.")
    summary.append(f"Columns: {', '.join(df.columns.tolist())}")

    summary.append("\nColumn Details:")
    for col in df.columns:
        dtype = df[col].dtype
        nulls = df[col].isnull().sum()
        summary.append(f"  - {col} (type: {dtype}, nulls: {nulls})")

    summary.append("\nNumeric Column Statistics:")
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) > 0:
        stats = df[numeric_cols].describe().round(2)
        summary.append(stats.to_string())
    else:
        summary.append("  No numeric columns found.")

    summary.append("\nSample Data (first 5 rows):")
    summary.append(df.head(5).to_string())

    return "\n".join(summary)