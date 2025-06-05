import streamlit as st

# Custom CSS for background and chat bubbles with rabbits
st.markdown("""
<style>
/* Light pink background */
body {
    background-color: #ffe4e6;
}

/* Container for the chat */
.chat-container {
    max-width: 700px;
    margin: 30px auto;
    padding: 20px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    font-family: 'Arial', sans-serif;
}

/* Chat bubbles */
.chatbox {
    padding: 12px 18px;
    border-radius: 15px;
    margin: 8px 0;
    max-width: 70%;
    font-size: 16px;
}
.user {
    background-color: #f8bbd0;
    margin-left: auto;
}
.bot {
    background-color: #fce4ec;
    margin-right: auto;
}

/* Title style */
.title {
    text-align: center;
    color: #c2185b;
    font-weight: bold;
    font-size: 2.5rem;
}

/* Rabbit images in corners */
.rabbit-top-left {
    position: fixed;
    top: 10px;
    left: 10px;
    width: 80px;
    opacity: 0.7;
    z-index: 9999;
}
.rabbit-bottom-right {
    position: fixed;
    bottom: 10px;
    right: 10px;
    width: 80px;
    opacity: 0.7;
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# Add rabbit images (you can replace these URLs with any cute rabbit image you prefer)
st.markdown("""
<img class="rabbit-top-left" src="https://i.postimg.cc/1XJwXpNC/cute-rabbit1.png" alt="rabbit top left">
<img class="rabbit-bottom-right" src="https://i.postimg.cc/4dCHbRsX/cute-rabbit2.png" alt="rabbit bottom right">
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">🐇 AI Therapist Chatbot 🐇</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>I'm here to listen and support you.</p>", unsafe_allow_html=True)

# Chat logic and UI
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    # Bot reply (you can expand this)
    if "sad" in user_input.lower():
        reply = "I'm sorry you're feeling sad. Remember, it's okay to have tough days."
    elif "happy" in user_input.lower():
        reply = "That's wonderful! What made you happy today?"
    elif "stress" in user_input.lower():
        reply = "Stress can be tough. Take a deep breath with me."
    else:
        reply = "Thanks for sharing. Tell me more about how you're feeling."
    st.session_state.messages.append({"role": "bot", "text": reply})

st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chatbox user">{msg["text"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chatbox bot">{msg["text"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

