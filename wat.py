import streamlit as st
import pandas as pd
from create import read
from datetime import datetime
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["Timestamp","RollNumber"])

ncol = st.session_state.df.shape[1] 
rw = -1

with st.form(key="add form", clear_on_submit= True):
   cols = st.columns(ncol)
   rwdta = []
   # while(True):
   thing=[datetime.now(),read()]
   for i in range(ncol):
      rwdta.append(thing[i])
   if st.form_submit_button("Add"):
      rw = st.session_state.df.shape[0] + 1
      st.session_state.df.loc[rw] = rwdta
      st.dataframe(st.session_state.df)
      