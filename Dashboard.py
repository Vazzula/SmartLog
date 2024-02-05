import streamlit as st
from st_on_hover_tabs import on_hover_tabs
from SupportPrograms import readsheet as rs
import pandas as pd
from PIL import Image
import time
from SupportPrograms import dummy 
import webbrowser

img=Image.open("E:\Padhai\Programs\Code\RFID\WebPage\Assets\SmartLogLogo2.png")

st.set_page_config (
    page_title="Dashboard",
    page_icon=img,
    layout="wide",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Welcome Admin!") 
st.subheader("\n")

with st.container():
    st.write("---")
    
with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.code("Do")