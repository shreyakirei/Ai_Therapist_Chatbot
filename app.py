import streamlit as st

st.title("AI Therapist Chatbot")

st.write("Hi! I’m here to listen. How are you feeling today?")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    text = user_input.lower()

    if any(word in text for word in ["sad", "unhappy", "depressed", "down", "miserable", "heartbroken"]):
        reply = (
            "I'm really sorry to hear that you're feeling this way. "
            "It's okay to feel sad sometimes. Remember, you're not alone — "
            "I'm here to listen whenever you need."
        )
    elif any(word in text for word in ["happy", "joy", "excited", "glad", "cheerful", "delighted", "content"]):
        reply = (
            "That's wonderful! Happiness is such a beautiful feeling. "
            "What’s something that made you feel this way today?"
        )
    elif any(word in text for word in ["stress", "anxious", "nervous", "worried", "overwhelmed", "tense"]):
        reply = (
            "Stress and anxiety can be really tough to manage. "
            "Have you tried any relaxation techniques like deep breathing or meditation? "
            "Taking small breaks can help too."
        )
    elif any(word in text for word in ["angry", "frustrated", "mad", "irritated", "annoyed", "upset"]):
        reply = (
            "Feeling angry or frustrated is completely natural. "
            "Would you like to talk more about what’s causing these feelings?"
        )
    elif any(word in text for word in ["lonely", "alone", "isolated", "left out", "abandoned"]):
        reply = (
            "Loneliness can be really hard. Remember, even if it feels like it, you are not alone. "
            "Talking about your feelings can sometimes help lighten the load."
        )
    elif any(word in text for word in ["tired", "exhausted", "sleepy", "drained", "fatigued"]):
        reply = (
            "It sounds like you’re feeling really tired. Rest and self-care are so important. "
            "Maybe try to take some time just for yourself."
        )
    elif any(word in text for word in ["confused", "lost", "uncertain", "doubtful", "unsure"]):
        reply = (
            "Feeling confused or unsure is okay — life can be complicated. "
            "Would you like to share more about what's causing this uncertainty?"
        )
    elif any(word in text for word in ["hopeful", "optimistic", "positive", "encouraged"]):
        reply = (
            "I’m glad to hear you're feeling hopeful! Holding onto positivity can really help in tough times."
        )
    else:
        reply = (
            "Thank you for sharing your feelings. "
            "Sometimes just talking about things helps. Would you like to continue?"
        )

    st.session_state.messages.append({"role": "bot", "text": reply})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**Therapist:** {msg['text']}")
