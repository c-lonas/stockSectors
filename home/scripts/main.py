import numpy as np
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go


# Get Data
data = yf.download(tickers='UBER', period='1d', interval="1m")

# Initialize Figure
g.figCandles = go.Figure()

# Candlestick 
g.figCandles.add_trace(go.Candlestick(x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close'], name='market-data'))

# figCandles.show()