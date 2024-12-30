import requests
import json

def emotion_detector(text_to_analyze):
    ''' Emotion detection application using the Watson NLP library 
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    empty_reponse = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
    }

    response = requests.post(url, json = myobj, headers = header)
    
    #Convert the response text into a dictionary
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        #Extract the required set of emotions, including anger, disgust, 
        #...fear, joy and sadness, along with their scores.
        emotions_list = formatted_response['emotionPredictions'][0]['emotion'].items()
        emotions_list = dict(emotions_list)

        #The code logic to find the dominant emotion (highest score).
        dominant_emotion = max(emotions_list, key=emotions_list.get)

        #add dominant_emotion to the strtructure
        emotions_list["dominant_emotion"] = dominant_emotion
        emotions = (dict(emotions_list))

        return emotions
    
    if response.status_code == 500:
        return empty_reponse

    if response.status_code == 400:
        return empty_reponse