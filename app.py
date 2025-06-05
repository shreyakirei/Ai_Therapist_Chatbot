import React, { useState } from 'react';

function App() {
  const [messages, setMessages] = useState([
    { from: 'bot', text: 'Hello! I’m your AI therapist. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');

  // Simulate AI response (replace with your AI API call)
  const getBotResponse = (userMessage) => {
    // For demo, bot repeats back user message after 1s delay
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`You said: "${userMessage}"`);
      }, 1000);
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { from: 'user', text: input }]);
    const userMessage = input;
    setInput('');

    // Get bot reply
    const botReply = await getBotResponse(userMessage);
    setMessages((prev) => [...prev, { from: 'bot', text: botReply }]);
  };

  return (
    <div style={{ maxWidth: 600, margin: '40px auto', fontFamily: 'Poppins, sans-serif' }}>
      <h2 style={{ textAlign: 'center' }}>CalmMind AI Therapist</h2>
      <div 
        style={{ 
          border: '1px solid #ddd', padding: 20, borderRadius: 10, height: 400, 
          overflowY: 'scroll', backgroundColor: '#f5f7fa' 
        }}
      >
        {messages.map((msg, i) => (
          <div 
            key={i} 
            style={{
              marginBottom: 15,
              textAlign: msg.from === 'user' ? 'right' : 'left'
            }}
          >
            <span style={{
              display: 'inline-block',
              backgroundColor: msg.from === 'user' ? '#c1dff7' : '#e0e7ff',
              color: '#333',
              padding: '10px 15px',
              borderRadius: 20,
              maxWidth: '70%'
            }}>
              {msg.text}
            </span>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} style={{ marginTop: 20, display: 'flex' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          style={{ flexGrow: 1, padding: 10, borderRadius: 20, border: '1px solid #ccc' }}
        />
        <button type="submit" style={{
          marginLeft: 10,
          padding: '10px 20px',
          borderRadius: 20,
          backgroundColor: '#6c63ff',
          color: '#fff',
          border: 'none',
          cursor: 'pointer'
        }}>Send</button>
      </form>
    </div>
  );
}

export default App;
