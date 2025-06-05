rom transformers import pipeline

emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

def detect_emotion(text):
    predictions = emotion_model(text)[0]
    predictions.sort(key=lambda x: x['score'], reverse=True)
    return predictions[0]['label'], predictions[0]['score']
