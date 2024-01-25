from gradio_client import Client
import cv2
import numpy as np 


client = Client("https://vikhyatk-moondream1.hf.space/--replicas/l0yi1/")
result = client.predict(
		"C:/Users/Admin/Pictures/Austin.png",	# filepath  in 'Upload or Drag an Image' Image component
		"what is in the image!!",	# str  in 'Question' Textbox component
		api_name="/answer_question"
)
print(result)

import  pyttsx3
import json, logging as log
log.basicConfig(level=log.INFO)

class text_to_speech_engine():
    def __init__(self, text_path, rate):
        self.text_path = text_path
        self.rate = rate

    def TTS(self):
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            log.info(self.text_path)
            log.info(engine.getProperty('rate'))
            engine.say(self.text_path)
            engine.runAndWait()
            engine.stop()
def speech_output(response):
        tts_engine = text_to_speech_engine(response, 150)
        tts_engine.TTS()
        log.info(response)

speech_output(result)