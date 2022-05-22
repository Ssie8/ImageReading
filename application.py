import streamlit as st
import easyocr
from PIL import Image
from numpy import asarray

st.title('Read Image')
reader = easyocr.Reader(['en'])
uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

if uploaded_file:
  # display the file
  display_image = Image.open(uploaded_file)
  numpydata = asarray(display_image)
  display_image = display_image.resize((500,300))
  st.image(display_image)
  pred_button = st.button('Read Image')
  
  if pred_button:
    prediction = reader.readtext(numpydata, detail = 0)
    st.text(f'Predictions: {prediction}')
