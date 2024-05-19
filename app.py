import streamlit as st 
from src.helper import DesktopAssistant
import os

GOOGLE_API_KEY = "AIzaSyCroY96R7FrCb9_gqT6mBadRJyGKsvDFrA"
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

DesktopAssistant = DesktopAssistant()

def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me anything!"):
        with st.spinner("Listening..."):
            text = DesktopAssistant.voice_input()
            response = DesktopAssistant.llm_model_object(text,GOOGLE_API_KEY)
            DesktopAssistant.text_to_speech(response)


            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()
            
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label="Download Speech",
                                data=audio_bytes,
                                file_name="speech.mp3",
                                mime="audio/mp3")









if __name__ == "__main__":
    main()

