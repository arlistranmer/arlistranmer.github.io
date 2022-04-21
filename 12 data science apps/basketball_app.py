import streamlit as st 
import pandas as pd 
import base64
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np 
""" Youtube video starting https://youtu.be/JwSS70SZdyM?t=2426 """
st.title('NBA Player Stats Explorer')

st.markdown(""" 
This app performs simple websraping of NBA player stats data!
* ** Python libraries: ** base64, pandas, streamlit 
* ** Data source: ** [Basketball-reference.com](https://www.basketball-reference.com/). """)

st.sidebar.header('User Input Features')
select_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))