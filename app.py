import streamlit as st

# CSS styling same as before (you can reuse from previous)

st.markdown("""
<style>
body {
    background-color: #ffe4e6;  /* soft light pink */
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #c94f7c;  /* dusty pink/mauve text */
    padding: 30px;
}
.title {
    font-size: 3.5rem;
    text-align: center;
    font-weight: 700;
    color: #d85c9f;
    text-shadow: 1px 1px 3px #f8bbd0;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    font-size: 1.5rem;
    font-style: italic;
    color: #e0a3b8;
    margin-bottom: 30px;
}
.chat-container {
    max-width: 700px;
    margin: auto;
    background: #fff0f6;
    border-radius: 20px;
    padding: 25px 40px;
    box-shadow: 0 6px 15px rgba(220, 158, 188, 0.3);
}
.user-msg {
    background-color: #f9d6e4;
    padding: 12px 18px;
    border-radius: 20px 20px 0 20px;
    margin: 10px 0;
    max-width: 70%;
    margin-left: auto;
    font-size: 1.1rem;
}
.bot-msg {
    background-color: #f7c6d9;
    padding: 12px 18px;
    border-radius: 20px 20px 20px 0;
    margin: 10px 0;
    max-width: 70%;
    margin-right: auto;
    font-size: 1.1rem;
}
input[type="text"] {
    padding: 10px;
    border-radius: 15px;
    border: 2px solid #d85c9f;
    width: 100%;
    font-size: 1.1rem;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
::placeholder {
    color: #e0a3b8;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🐰 AI Therapist Chatbot 🐰</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Soft ears, soft words — I’m here to listen.</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", placeholder="Tell me how you’re feeling...", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    text = user_input.lower()
    # More emotions & replies
    if any(word in text for word in ["sad", "unhappy", "down", "depressed", "lonely"]):
        reply = "I'm really sorry you're feeling sad. Remember, it's okay to have tough days. I'm here for you. 💖"
    elif any(word in text for word in ["happy", "joy", "glad", "excited", "cheerful", "great"]):
        reply = "That's wonderful to hear! What made you feel so happy today? 😊"
    elif any(word in text for word in ["stress", "anxious", "worried", "nervous", "tense"]):
        reply = "Stress and anxiety can be tough. Try to take some deep breaths with me. You're not alone. 🌸"
    elif any(word in text for word in ["angry", "frustrated", "annoyed", "mad"]):
        reply = "It's okay to feel angry sometimes. Want to talk about what’s bothering you? 🐇"
    elif any(word in text for word in ["tired", "exhausted", "sleepy", "fatigued"]):
        reply = "You sound really tired. Make sure to rest and take care of yourself. Your wellbeing matters. 🌙"
    elif any(word in text for word in ["confused", "lost", "uncertain", "unsure"]):
        reply = "Feeling confused is normal. Take your time — I’m here whenever you want to chat. 💕"
    elif any(word in text for word in ["grateful", "thankful", "blessed"]):
        reply = "Gratitude is such a beautiful feeling. What are you thankful for today? 🌷"
    elif any(word in text for word in ["hopeful", "optimistic", "positive"]):
        reply = "I love your positive vibe! Keep holding onto that hope. 🌞"
    elif any(word in text for word in ["lonely", "alone"]):
        reply = "You’re not alone, even if it feels that way. I’m here to listen. 🐰"
    else:
        reply = "Thanks for sharing. Tell me more about how you're feeling. 🥰"

    st.session_state.messages.append({"role": "bot", "text": reply})

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
