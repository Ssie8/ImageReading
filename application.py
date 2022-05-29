import streamlit as st
import os
from gtts import gTTS
import easyocr
from PIL import Image
from numpy import asarray
from googletrans import Translator

st.title('Image Reading')
with st.expander("ℹ️ - About this app", expanded=True):
  st.write("This App can read english text inside of images and translate it to italian. Please upload an image")
reader = easyocr.Reader(['en'])
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
translator = Translator()

if uploaded_file:
    # display the file
    display_image = Image.open(uploaded_file)
    numpydata = asarray(display_image)
    display_image = display_image.resize((500,300))
    st.image(display_image)
    pred_button = st.button('Read Image')
    
    if pred_button:
        prediction = ' '.join(reader.readtext(numpydata, detail = 0))
        st.text(f'Predictions: {prediction}')
        tts = gTTS(text=prediction)
        tts.save('en_audio.mp3')
        audio_file = open('en_audio.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
        st.header('Translated to Italian')
        it_result = translator.translate(prediction, dest='it')
        st.text(it_result.text)
        tts_it = gTTS(text=it_result.text, lang='it')
        tts_it.save('it_audio.mp3')
        audio_file = open('it_audio.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
