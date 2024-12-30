''' Emotion Detection app
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' This code has a text input from the HTML interface and 
        runs emotion detector. 
        The output returned the result of the emotion analysis 
        and mention the dominant oemotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!. "
    # Extracting the dominant emotion
    dominant_emotion = response.pop("dominant_emotion")
    # Constructing the response string
    response_formatted = "For the given statement, the system response is "
    response_formatted += ", ".join([f"'{key}': {value}" for key, value in response.items()])
    response_formatted += f". The dominant emotion is {dominant_emotion}."

    return response_formatted

@app.route("/")
def render_index_page():
    ''' This function renders the index.html page
    '''

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
