def generate_response(emotion):
    responses = {
        "joy": "That's wonderful! What made you feel happy today?",
        "sadness": "I'm really sorry you're feeling this way. Want to talk about it?",
        "anger": "It's okay to feel angry. Let’s try taking a deep breath together.",
        "fear": "That sounds scary. You're safe here with me.",
        "love": "Love is beautiful. Who are you thinking of?",
        "surprise": "Oh wow! That must’ve been unexpected. Tell me more.",
        "neutral": "I'm listening. How's your day going?"
        "tired": "AWW i totally understand you probably should get some rest."
    }
    return responses.get(emotion.lower(), "I'm here for you. Feel free to share more.")
