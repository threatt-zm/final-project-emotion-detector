"""
    importing the necessary module to create a Flask app.
    Also importing the emotion_detector() method to use within the application
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emot_detector():
    """
        method that collects the users text input and analyze it for emotion scores.
        It prints an error message when an input is not given,
        and a success message based on the input given 
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""
    For the given statement, the system response is 'anger': {anger_score},
    'disgust': {disgust_score},
    'fear': {fear_score},
    'joy': {joy_score}
    and 'sadness': {sadness_score}.
    The dominant emotion is {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    """
        method to render the index.html page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
