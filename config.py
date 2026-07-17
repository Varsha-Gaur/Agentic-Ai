import streamlit as st

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
BASE_URL = st.secrets["BASE_URL"]
MODEL_NAME = st.secrets["MODEL_NAME"]
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# Used by tools/stock_tool.py (Yahoo Finance — free, no key required)
STOCK_API_URL = "https://query1.finance.yahoo.com/v8/finance/chart/"
STOCK_SEARCH_URL = "https://query1.finance.yahoo.com/v1/finance/search"

# Used by tools/currency_tool.py (Frankfurter — free, ECB rates, no key required)
CURRENCY_API_URL = "https://api.frankfurter.app/latest"
