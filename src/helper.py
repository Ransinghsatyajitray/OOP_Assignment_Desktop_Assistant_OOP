import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS



class DesktopAssistant:
    def __init__(self):
        pass
        
    def voice_input(self):
        # Create a recognizer instance
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)  # Using Google Speech Recognition
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    def text_to_speech(self, text: str):
        self.text = text
        # Create a gTTS object
        tts = gTTS(text=self.text, lang='en')  # Language can be changed

        # Save the audio as an MP3 file
        tts.save("speech.mp3")

    def llm_model_object(self, user_text: str, googleapikey: str):
        self.user_text = user_text
        
        genai.configure(api_key = googleapikey)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(self.user_text)
        result = response.text
        
        return result
    