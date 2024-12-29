import requests
import json

def emotion_detector(text_to_analyze):
    ''' Emotion detection application using the Watson NLP library 
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    #emotions = ['emotionPredictions'][0]['emotion'].items()
    #for emotion, score in emotions:
    #    for emotion, score in emotions:
    #for x in len(['emotionPredictions'][0]['emotion']):
    #    emotions.append(['emotionPredictions'][0]['emotion'][x])

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    #for x in (anger_score, disgust_score, fear_score, joy_score, sadness_score):
    #    if 

    #dominant_emotion = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

    return response.text