"""Flask API for Emotion Detection"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
import requests

app = Flask(__name__)

@app.route("/")
def home():
    """Renders the homepage with input form"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """
    Processes text input and returns emotion analysis result in a formatted string.
    """
    text = request.args.get("text")
    if not text:
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text)

        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!", 400

        response_str = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )
        return response_str

    except (requests.exceptions.RequestException, ValueError, TypeError) as error:
        return f"Error processing request: {str(error)}", 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
