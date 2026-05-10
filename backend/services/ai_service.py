import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_data(question: str, data_summary: str) -> str:
    system_prompt = f"""You are an expert Business Intelligence analyst.
The user has uploaded a dataset. Here is the full summary of the data:

{data_summary}

Your job is to:
- Answer questions about this data clearly and accurately
- Give insights, trends, and patterns
- If asked for calculations, compute them from the data
- Keep answers concise and useful
- If the question is not related to the data, politely redirect the user
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

