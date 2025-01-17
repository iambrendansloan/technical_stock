{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1125d173-fdf0-4879-836f-bb0696ecdbf5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import streamlit as st\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "st.title('Stock Price App')\n",
    "\n",
    "# Get ticker symbol from user input\n",
    "ticker_symbol = st.text_input(\"Enter Ticker Symbol (e.g., AAPL, GOOGL)\")\n",
    "\n",
    "# Fetch data\n",
    "if ticker_symbol:\n",
    "    ticker_data = yf.Ticker(ticker_symbol)\n",
    "    df = ticker_data.history(period=\"1y\")\n",
    "\n",
    "    # Calculate technical indicators\n",
    "    df['SMA_50'] = df['Close'].rolling(window=50).mean()\n",
    "    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()\n",
    "\n",
    "    # Create candlestick chart\n",
    "    fig = go.Figure(data=[go.Candlestick(x=df.index,\n",
    "                                       open=df['Open'],\n",
    "                                       high=df['High'],\n",
    "                                       low=df['Low'],\n",
    "                                       close=df['Close'])])\n",
    "\n",
    "    # Add moving averages\n",
    "    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], name='SMA 50'))\n",
    "    fig.add_trace(go.Scatter(x=df.index, y=df['EMA_20'], name='EMA 20'))\n",
    "\n",
    "    # Customize chart\n",
    "    fig.update_layout(title=f'{ticker_symbol} Stock Price',\n",
    "                      xaxis_rangeslider_visible=True)\n",
    "\n",
    "    st.plotly_chart(fig)\n",
    "\n",
    "# Handle potential NameError for execution_count\n",
    "try:\n",
    "    # Code that might raise NameError\n",
    "    execution_count = null  # Replace 'null' with the actual variable or expression\n",
    "except NameError:\n",
    "    print(\"Variable 'execution_count' is not defined.\")\n",
    "    # Handle the error, e.g., assign a default value or skip the operation\n",
    "    execution_count = 0  # Or any other appropriate value"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
