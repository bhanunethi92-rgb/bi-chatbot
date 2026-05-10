import { useState } from "react"
import axios from "axios"
import "./App.css"

function App() {
  const [file, setFile] = useState(null)
  const [uploaded, setUploaded] = useState(false)
  const [question, setQuestion] = useState("")
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)
  const [fileInfo, setFileInfo] = useState(null)

  const handleUpload = async () => {
    if (!file) return alert("Please select a file first!")
    const formData = new FormData()
    formData.append("file", file)
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/upload", formData)
      setUploaded(true)
      setFileInfo(res.data)
      setMessages([{ role: "bot", text: `✅ File "${res.data.filename}" uploaded! ${res.data.rows} rows, ${res.data.columns.length} columns. Ask me anything about your data!` }])
    } catch (err) {
      alert("Upload failed! Make sure backend is running.")
    }
  }

  const handleChat = async () => {
    if (!question.trim()) return
    const userMsg = { role: "user", text: question }
    setMessages(prev => [...prev, userMsg])
    setQuestion("")
    setLoading(true)
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/chat", { question })
      setMessages(prev => [...prev, { role: "bot", text: res.data.answer }])
    } catch (err) {
      setMessages(prev => [...prev, { role: "bot", text: "Error! Please try again." }])
    }
    setLoading(false)
  }

  const handleKeyPress = (e) => {
    if (e.key === "Enter") handleChat()
  }

  return (
    <div className="app">
      <div className="header">
        <h1>📊 BI Chatbot</h1>
        <p>Upload your CSV/Excel file and ask questions!</p>
      </div>

      <div className="upload-section">
        <input type="file" accept=".csv,.xlsx,.xls" onChange={e => setFile(e.target.files[0])} />
        <button onClick={handleUpload} className="upload-btn">Upload File</button>
        {fileInfo && <span className="file-info">✅ {fileInfo.filename} ({fileInfo.rows} rows)</span>}
      </div>

      <div className="chat-window">
        {messages.length === 0 && (
          <div className="empty-state">Upload a file to start chatting! 👆</div>
        )}
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <span className="avatar">{msg.role === "user" ? "👤" : "🤖"}</span>
            <div className="bubble">{msg.text}</div>
          </div>
        ))}
        {loading && (
          <div className="message bot">
            <span className="avatar">🤖</span>
            <div className="bubble">Thinking...</div>
          </div>
        )}
      </div>

      <div className="input-section">
        <input
          type="text"
          placeholder={uploaded ? "Ask a question about your data..." : "Upload a file first..."}
          value={question}
          onChange={e => setQuestion(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={!uploaded}
        />
        <button onClick={handleChat} disabled={!uploaded || loading} className="send-btn">Send</button>
      </div>
    </div>
  )
}

export default App