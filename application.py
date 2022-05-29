import streamlit as st
import easyocr
from gtts import gTTS
from PIL import Image
from numpy import asarray
from googletrans import Translator

st.title('Read Image')
with st.expander("ℹ️ - About this app", expanded=True):
  st.write("This App can read text inside of images")
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
    prediction = reader.readtext(numpydata, detail = 0)
    prediction_2 = ' '.join(prediction)
    st.text(f'Text inside image: {prediction_2}')
    tts = gTTS(text=prediction_2)
    tts.save('audio.mp3')
    audio_file = open('audio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)
    st.header('Translated to Italian')
    it_result = translator.translate(prediction_2, dest='it')
    st.text(it_result.text)
    tts = gTTS(text=it_result.text, lang='it')
    tts.save('it_audio.mp3')
    audio_file = open('it_audio.mp3', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes)
