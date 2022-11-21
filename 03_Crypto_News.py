import requests
from bs4 import BeautifulSoup
import streamlit as st

url='https://www.livemint.com/market/cryptocurrency'
response = requests.get(url)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://1.bp.blogspot.com/-hsAA88aKmAg/YBMpLKgMTgI/AAAAAAAAeaI/W6jwgSuW55cSO9lsg7uKumAh4Yq7yDnCwCLcBGAsYHQ/w296-h640/heroscreen.cc-V1-01282021-stock-market-phone-wallpaper-HD.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')

st.header("Market News Updates")

i = 1
for x in headlines:
    st.text(i)
    st.subheader(x.text.strip())
    i += 1
