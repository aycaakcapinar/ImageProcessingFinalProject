import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
import glob
from os import listdir
from math import ceil
import os
import requests
from streamlit_image_select import image_select
from color_palette import find_color_palette
from virtual_makeup import main

st.title('Coloring Virtual Make-ups Based on MovieScenes')

upload_file = st.file_uploader('Upload a image you want to try virtual makeup')
if upload_file is not None:
    st.image(upload_file)

#st.sidebar.title('Virtual Makeup')
# st.sidebar.subheader('Movies')

#img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(
#         bytes_data, np.uint8), cv2.IMREAD_COLOR)

#     # Check the type of cv2_img:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(cv2_img))

#     # Check the shape of cv2_img:
#     # Should output shape: (height, width, channels)
#     st.write(cv2_img.shape)


out_folder = "movie_scenes"
images = []
for i in os.listdir(out_folder):
    if i.endswith(("jpg", "jpeg", "png")):
        #image = Image.open(os.path.join(out_folder, i))
        # st.sidebar.image(new_image, caption=i)
        images.append(os.path.join(out_folder, i))


img = image_select("Lets choose movie", images)
st.write(img)
if img is not None and upload_file is not None:
    colors, percent = find_color_palette(img)
    makeup_image = main(upload_file, colors)
    print(colors)
