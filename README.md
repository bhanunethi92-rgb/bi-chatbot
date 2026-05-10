# 📊 AI-Powered Business Intelligence Chatbot

An intelligent chatbot that allows users to upload CSV/Excel files and ask natural language questions about their data. Powered by Groq's Llama 3.3 AI model.

![Tech Stack](https://img.shields.io/badge/Python-FastAPI-009688?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react)
![AI](https://img.shields.io/badge/AI-Groq%20Llama%203.3-orange?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas)

---

## 🚀 Features

- 📁 Upload CSV or Excel files
- 💬 Ask questions in plain English
- 🤖 AI-powered business insights
- 📈 Trends, patterns & statistics
- ⚡ Fast responses with Groq AI
- 🎨 Clean dark-themed chat UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React + Vite + Axios |
| Backend | Python + FastAPI |
| Data Processing | Pandas |
| AI Model | Groq (Llama 3.3 70B) |
| Server | Uvicorn |

---

## 📁 Project Structure

```
bi-chatbot/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── .env                 # API keys (not committed)
│   ├── routes/
│   │   ├── upload.py        # File upload endpoint
│   │   └── chat.py          # Chat endpoint
│   └── services/
│       ├── data_service.py  # Pandas data processing
│       └── ai_service.py    # Groq AI integration
│
└── frontend/
    └── src/
        ├── App.jsx          # Main React component
        └── App.css          # Styling
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9+
- Node.js 18+
- Groq API key (free at [console.groq.com](https://console.groq.com))

### 1. Clone the repository
```bash
git clone https://github.com/bhanunethi92-rgb/bi-chatbot.git
cd bi-chatbot
```

### 2. Backend Setup
```bash
cd backend
pip install fastapi uvicorn pandas openpyxl python-multipart groq python-dotenv
```

Create `.env` file in backend folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

Run backend:
```bash
py -m uvicorn main:app --reload
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm install axios
npm run dev
```

### 4. Open in Browser
```
http://localhost:5173
```

---

## 💡 How to Use

1. Open `http://localhost:5173`
2. Click **Choose File** and select a CSV or Excel file
3. Click **Upload File**
4. Type your question in the chat box
5. Press **Enter** or click **Send**

### Example Questions
- *"Which month had the highest profit?"*
- *"What is the total sales for all months?"*
- *"Which region performed the best?"*
- *"Give me a complete business summary"*
- *"What are the top 3 months by revenue?"*

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/upload` | Upload CSV/Excel file |
| POST | `/api/chat` | Ask a question about data |
| GET | `/api/data-info` | Get uploaded file info |
| GET | `/docs` | Swagger API documentation |

---

## 🖥️ Screenshots

### Chat Interface
- Clean dark-themed UI
- File upload with status indicator
- Real-time AI responses
- Message history

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License — free to use and modify.

---

## 👨‍💻 Author

**BhanuTeja** — [GitHub](https://github.com/bhanunethi92-rgb)

---

⭐ **Star this repo if you found it useful!**
# bi-chatbot
AI-powered Business Intelligence Chatbot | Upload CSV/Excel files and ask questions in natural language | Built with Python FastAPI, React, Pandas, and Groq Llama 3.3 AI
