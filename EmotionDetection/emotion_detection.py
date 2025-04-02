import requests
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    result = response.json()
    # Extract emotion scores
    emotion_scores = result["emotionPredictions"][0]["emotion"]
    # Focus only on required emotions
    selected_emotions = {
        'anger': emotion_scores.get('anger', 0),
        'disgust': emotion_scores.get('disgust', 0),
        'fear': emotion_scores.get('fear', 0),
        'joy': emotion_scores.get('joy', 0),
        'sadness': emotion_scores.get('sadness', 0)
    }
    # Determine the dominant emotion
    dominant = max(selected_emotions, key=selected_emotions.get)
    selected_emotions['dominant_emotion'] = dominant
    return selected_emotions