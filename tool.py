import requests
from bs4 import BeautifulSoup
import streamlit as st
from random import choice
from urllib.parse import urlencode

st.title("Random Backlog Link Tweeter")

url = st.text_input("sitemap URL")

st.button("Pick Another")

if url:
    sitemap = requests.get(url)
    soup = BeautifulSoup(sitemap.text, features="html.parser")

    pages = [el.text for el in soup.find_all("loc")]

    page = choice(pages)

    soup = BeautifulSoup(requests.get(page).text, features="html.parser")

    title = soup.find("meta", property="og:title")
    if title:
        title = title["content"]
    else:
        title = "[no title found]"
    query = urlencode({"text": title, "url": page})
    tlink = "https://twitter.com/intent/tweet?" + query

    st.write("Click the link below to tweet.")
    st.write(f"[{title}]({tlink})")




