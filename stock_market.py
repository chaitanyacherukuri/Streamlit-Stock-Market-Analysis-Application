import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import datetime

st.title('Stock Market Analysis')

st.write('This is my first streamlit application')



ticker_symbol = st.text_input('Enter Stock Ticker', 'TSLA')

ticker_data = yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    sd = st.date_input('Starting Date', datetime.date(2023, 1, 1))

with col2:
    ed = st.date_input('Ending Date', datetime.date(2024, 1, 1))

# get historical market data
hist = ticker_data.history(period="1d", start = f'{sd}', end = f'{ed}')

ticker_df = hist.reset_index()

st.write(f'We are viewing stock info for {ticker_symbol}')

st.write(ticker_df)

col1, col2 = st.columns(2)

with col1:
    st.header('Volume Analysis')
    #st.line_chart(hist['Volume'])
    st.line_chart(ticker_df, x = 'Date', y = 'Volume')

with col2:
    st.header('Closing Price Analysis')
    #st.line_chart(hist['Close'])
    st.line_chart(ticker_df, x = 'Date', y = 'Close')


