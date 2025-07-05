import React, { useState } from "react";
import axios from "axios";

const API_BASE = "https://banking-backend-vjmt.onrender.com";

export default function BankingSolver() {
  const [user, setUser] = useState({ name: "", mobile: "", chapter: "Banking" });
  const [chat, setChat] = useState([]);
  const [input, setInput] = useState("");
  const [image, setImage] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [summary, setSummary] = useState("");
  const [practiceQuestion, setPracticeQuestion] = useState("");
  const [mockTest, setMockTest] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  const handleChatSubmit = async () => {
    let question = input;

    if (image) {
      const formData = new FormData();
      formData.append("image", image);
      try {
        const res = await axios.post(`${API_BASE}/ocr`, formData);
        question = res.data.text;
      } catch (error) {
        setChat([...chat, { role: "bot", message: "❌ Error processing image." }]);
        return;
      }
    }

    const updatedChat = [...chat, { role: "user", message: question }];
    setChat(updatedChat);
    setInput("");
    setImage(null);

    try {
      const res = await axios.post(`${API_BASE}/solve`, {
        chapter: user.chapter,
        question,
      });
      setChat([...updatedChat, { role: "bot", message: res.data.answer }]);
    } catch (error) {
      setChat([...updatedChat, { role: "bot", message: "❌ Server error." }]);
    }
  };

  const fetchSummary = async () => {
    const res = await axios.get(`${API_BASE}/summary`);
    setSummary(res.data.summary);
  };

  const fetchPracticeQuestion = async () => {
    const res = await axios.get(`${API_BASE}/generate-question`);
    setPracticeQuestion(res.data.question);
  };

  const fetchMockTest = async () => {
    const res = await axios.get(`${API_BASE}/mock-test`);
    setMockTest(res.data);
  };

  if (!submitted) {
    return (
      <div style={{ padding: "2rem", maxWidth: "500px", margin: "auto" }}>
        <h2>Enter Your Details</h2>
        <input type="text" placeholder="Your Name" value={user.name}
          onChange={(e) => setUser({ ...user, name: e.target.value })} />
        <input type="text" placeholder="Mobile Number" value={user.mobile}
          onChange={(e) => setUser({ ...user, mobile: e.target.value })} />
        <button onClick={() => setSubmitted(true)}>Continue</button>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "800px", margin: "auto", padding: "2rem" }}>
      <h2>Ask your Banking Chapter Doubt</h2>
      {chat.map((c, i) => (
        <div key={i} style={{
          backgroundColor: c.role === "user" ? "#e6f7ff" : "#f6ffed",
          padding: "10px", borderRadius: "6px", marginBottom: "8px"
        }}>
          <strong>{c.role === "user" ? "You" : "AI"}:</strong><br />
          <span style={{ whiteSpace: "pre-wrap" }}>{c.message}</span>
        </div>
      ))}

      <textarea placeholder="Type your question..." rows={3} value={input}
        onChange={(e) => setInput(e.target.value)} style={{ width: "100%", padding: "8px" }} />

      <div style={{ display: "flex", gap: "1rem", marginTop: "10px" }}>
        <input type="file" accept="image/*" onChange={handleImageUpload} />
        <button onClick={handleChatSubmit}>Ask</button>
      </div>

      <div style={{ marginTop: "20px" }}>
        <button onClick={fetchSummary}>📘 Show Summary</button>
        <button onClick={fetchPracticeQuestion}>🧠 Practice Question</button>
        <button onClick={fetchMockTest}>📝 Mock Test</button>
      </div>

      {summary && <div><h3>Summary</h3><pre>{summary}</pre></div>}
      {practiceQuestion && <div><h3>Try This</h3>{practiceQuestion}</div>}
      {mockTest && (
        <div>
          <h3>Mock Test</h3>
          {mockTest.questions.map((q, index) => (
            <div key={index}>
              <p><strong>Q{index + 1}:</strong> {q.question} ({q.marks} marks)</p>
              <ul>
                {Object.entries(q.marking_scheme).map(([step, mark], i) => (
                  <li key={i}>{step}: {mark} mark(s)</li>
                ))}
              </ul>
              <details><summary>Answer</summary><pre>{q.answer}</pre></details>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
