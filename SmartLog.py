import streamlit as st
from PIL import Image
import pandas as pd
import time
# from SupportPrograms import ReadDBToDF as dd
from st_on_hover_tabs import on_hover_tabs
from SupportPrograms import Server_PC
from datetime import datetime

img=Image.open("E:\Padhai\Programs\Code\RFID\WebPage\Assets\SmartLogLogo2.png")

st.set_page_config (
    page_title="SmartLog",
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

st.markdown('<style>' + open('E:\Padhai\Programs\Code\RFID\WebPage\SupportPrograms\style.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Smart Log', 'Read', 'Login'], 
                         iconName=['dashboard', 'book', 'person'],default_choice=0)

if tabs =='Smart Log':
    st.title("Smart Log Systems")
    st.subheader("A Project by 21881A12G6 | 21881A12K0 | 21881A12G3 | 21881A12G5 |21881A12H8 | 21881A12K1")

    with st.container():
        st.write("---")
        leftColumn,rightColumn=st.columns(2)

        with leftColumn:
            st.write("##");
            st.markdown("<p style='text-align: justify; line-height:50px; font-size:45px;'>About the project",unsafe_allow_html=True)        
            st.markdown("<p style='text-align: justify; line-height:50px; font-size:30px;'>This project is to ease the process of Lab and Inventory management using RFID Technology to maintain Smart Logs of Equipment and the concepts learned through the courses: <br>Internet of Things (IoT) <br>Database Management Systems (DBMS)</p>",unsafe_allow_html=True)

        with rightColumn:
            img=Image.open("E:\Padhai\Programs\Code\RFID\WebPage\Assets\SmartLog1.png")
            st.image(img,width=500) 

elif tabs == 'Read':
    st.title("Read")
    st.subheader("Reading RFID Encrypted data into the Database\n")

    with st.container():
        st.write("---")
        st.markdown("<p style='text-align: justify; line-height:50px; font-size:25px;'>The following tables are near live displays of the RFID based lab equipment monitoring<br><br>",unsafe_allow_html=True)
    
    with st.container():
        form1=st.form(key="Options")
        with form1:
            st.header("Enter Details")
            year=st.multiselect("Enter Year:",["I","II","III","IV"],key=1,max_selections=1)
            stream=st.multiselect("Enter Stream:",["CSE","IT","MECH","CIVIL","CSM","AIDS","ECE","EEE"],key=2,max_selections=1)
            section=st.multiselect("Enter Section:",["NIL","A","B","C","D"],key=3,max_selections=1)
            
            submitted1 = st.form_submit_button("Start Reading")
            
        with st.container():
            col1,col2=st.columns(2)
            with col1:
                with st.form(key="Rollnumber", clear_on_submit= True):
                    st.subheader("Student Log")
                    df=pd.DataFrame({"SNO":[42,43],
                     "TimeStamp":["09-04-2023 12:30","09-04-2023 12:31"],
                     "Rollnumber":["21881A12G6","21881A12K0"]
                    })
                    if st.form_submit_button("Refresh"):
                        st.table(df)
            with col2:
                with st.form(key="Equipment", clear_on_submit= True):
                    st.subheader("Equipment Log")
                    df=pd.DataFrame({"SNO":[40,41,42],
                     "Equipment":["equipment2","equipment1","equipment3"],
                     "Rollnumber":["21881A12G6","21881A12K0","21881A12K0"]
                    })
                    if st.form_submit_button("Refresh"):
                        st.table(df)
  
elif tabs == 'Login':
    
    st.title("Login") 
    
    username="Admin"
    password="root"

    with st.form("Login"):
        st.markdown("#### Enter your credentials")
        user= st.text_input("Username")
        userpassword = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit and (username!=user or password!=userpassword):
            st.error("Incorrect Username/Password")
        elif submit and (username==user and password==userpassword):
            st.success("User Verified Redirecting...")
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
    if(submit and (username==user and password==userpassword)):
                    st.subheader("Pending Log")
                    df=df=pd.DataFrame({"SNO":[42],
                     "TimeStamp":["equipment3"],
                     "Rollnumber":["21881A12K0"]
                    })
                    st.table(df)
                
                
            