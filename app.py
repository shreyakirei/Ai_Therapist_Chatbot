import streamlit as st

st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe4e6, #f9d7db);
    font-family: 'Comic Sans MS', cursive, sans-serif;
    color: #8b3a4a;  /* warm mauve */
    padding: 40px 20px;
    min-height: 100vh;
    margin: 0;
}
.title {
    font-size: 3.8rem;
    text-align: center;
    font-weight: 800;
    color: #d26b7f;
    text-shadow: 2px 2px 6px #f7a1b5cc;
    margin-bottom: 15px;
    user-select: none;
}
.subtitle {
    text-align: center;
    font-size: 1.6rem;
    font-style: italic;
    color: #c37b8e;
    margin-bottom: 40px;
    user-select: none;
}
.chat-container {
    max-width: 700px;
    margin: auto;
    background: #fff0f2;
    border-radius: 25px;
    padding: 30px 45px;
    box-shadow:
        0 8px 20px rgba(210, 105, 135, 0.25),
        inset 0 0 15px #f9c6d1;
}
.user-msg {
    background-color: #f9a8b8;  /* cozy pink */
    padding: 14px 22px;
    border-radius: 25px 25px 0 25px;
    margin: 12px 0;
    max-width: 70%;
    margin-left: auto;
    font-size: 1.15rem;
    color: #4c2a38;
    box-shadow: 1px 2px 7px #e89ca7aa;
    word-wrap: break-word;
    line-height: 1.4;
}
.bot-msg {
    background-color: #f2c4ce;  /* gentle pastel pink */
    padding: 14px 22px;
    border-radius: 25px 25px 25px 0;
    margin: 12px 0;
    max-width: 70%;
    margin-right: auto;
    font-size: 1.15rem;
    color: #4c2a38;
    box-shadow: 1px 2px 7px #dba3adcc;
    word-wrap: break-word;
    line-height: 1.4;
}
input[type="text"] {
    padding: 14px 18px;
    border-radius: 20px;
    border: 3px solid #d36a7a;
    width: 100%;
    font-size: 1.15rem;
    font-family: 'Comic Sans MS', cursive, sans-serif;
    outline: none;
    box-shadow: 0 0 8px #f3a7bc66;
    transition: box-shadow 0.3s ease;
}
input[type="text"]:focus {
    box-shadow: 0 0 14px #e96e8baa;
    border-color: #e96e8b;
}
::placeholder {
    color: #d29ba8;
    font-style: italic;
    user-select: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">♡ Kawaii Ai Therapist ♡</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Soft ears, soft words — I’m here to listen.</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", placeholder="Tell me how you’re feeling...", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    text = user_input.lower()
    # Emotions handling (unchanged)
    if any(word in text for word in ["sad", "unhappy", "down", "depressed", "lonely","gloomy", "sorrow", "hate", "low"]):
        reply = "I'm really sorry you're feeling sad. Remember, it's okay to have tough days. I'm here for you. 💖"
    elif any(word in text for word in ["happy", "joy", "glad", "excited", "cheerful", "great", "blissful", "ecstatic"]):
        reply = "That's wonderful to hear! What made you feel so happy today?"

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
