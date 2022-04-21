import yfinance as yf
import streamlit as st
import pandas as pd

""" 
Open terminal and open in browser by typing : streamlit run StockPrice.py
To make sure you are connected to streamlit say: streamlit hello 
 """

""" 
Links to customize this app 
Youtube video tutorial = https://www.youtube.com/watch?v=JwSS70SZdyM&t=5786s
github library with all of the original code = https://github.com/dataprofessor/streamlit_freecodecamp/find/main
yfinance documentation = https://openbase.com/python/yfinance/documentation
markdown cheat sheat = https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
 """
st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol

tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(""" ## Closing Price """)
st.line_chart(tickerDf.Close)
st.write(""" ## Volume Price """)
st.line_chart(tickerDf.Volume)
st.write(""" ## Earings """)
tickerData.earnings
st.write(""" ## Options Expiration """)
tickerData.options
