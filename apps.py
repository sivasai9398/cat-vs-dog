import streamlit as st
import numpy as np
from tensorflow.keras import models
import cv2
import io
from PIL import Image
import win32com.client
CATEGORIES = ['Cat', 'Dog']
def image(path):
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    st.write("HELLO all how are you hope all are fine in this pandemic situation")
    s="HELLO all how are you hope all are fine in this pandemic situation"
    speaker.Speak(s)
    st.image(path,width=600)
    image = np.array(path)
    imagess=cv2.imwrite('out.jpg',image)
    images=cv2.imread('out.jpg',cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    new_arr = cv2.resize(images, (60, 60))
    new_arr = np.array(new_arr)
    new_arr = new_arr.reshape(-1, 60, 60, 1)
    new_arr=new_arr.astype('float64')
    model = models.load_model(r'C:\Users\sivasai\Downloads\3x3x64-catvsdog.model')
    prediction=model.predict(new_arr)
    if np.argmax(prediction)==0:
        val="cat"
    else:
        val="dog"
    return val
def main():
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    #st.write("HELLO all how are you hope all are fine in this pandemic situation")
    #s="HELLO all how are you hope all are fine in this pandemic situation"
    #speaker.Speak(s)
    st.write("Welcome to this page")
    image_file=st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])
    if image_file is not None:
                    text_io = io.TextIOWrapper(image_file)
                    st.set_option('deprecation.showfileUploaderEncoding', False)
                    img = Image.open(image_file)
                    if st.button("Process"):
                        val=image(img)
                        st.write("image detected is",val)
                        w="image detected is"+str(val)
                        speaker.Speak(w)
                     
                        #st.image(res_image,width=600)
if __name__=="__main__":
    main()