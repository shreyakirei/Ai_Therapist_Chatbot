import streamlit as st

st.title("AI Therapist Chatbot")

st.write("Hi! I’m here to listen. How are you feeling today?")

# To keep chat history during session
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input text box
user_input = st.text_input("You:", key="input")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "text": user_input})
    
    # Simple rule-based reply (you can replace with AI model)
    if "sad" in user_input.lower():
        reply = "I'm sorry you're feeling sad. Remember, it's okay to have tough days."
    elif "happy" in user_input.lower():
        reply = "That's great to hear! What made you happy today?"
    elif "stress" in user_input.lower():
        reply = "Stress can be overwhelming. Try taking a few deep breaths with me."
    else:
        reply = "Thanks for sharing. Tell me more about how you're feeling."

    # Add bot reply to chat history
    st.session_state.messages.append({"role": "bot", "text": reply})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**Therapist:** {msg['text']}")
