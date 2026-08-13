import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image
from sklearn.cluster import KMeans
from palette import create_color_palette
from PIL import Image
import numpy as np


st.header("Dominant Color Finder")

uploaded_file = st.file_uploader("Choose a file")

col1,col2 = st.columns(2)

if uploaded_file is not None:
    with col1:
        st.subheader("Uploaded File")
        st.image(uploaded_file)
    
    with col2:
        st.subheader("Dominant Colors")
        image = Image.open(uploaded_file).convert("RGB")        
        image = np.array(image)
        X = image.reshape(-1,3)
        
        kmeans = KMeans(n_clusters=5,random_state=42)
        kmeans.fit(X)
        
        dominant_colors = kmeans.cluster_centers_.astype(int)            
        palette = create_color_palette(dominant_colors)
        st.image(palette,width=700)
        
        
   