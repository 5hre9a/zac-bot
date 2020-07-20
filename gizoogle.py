"""
Retrieve a gizoogled string. Mostly adapted from a library written in ruby.
Optimized for python3.
"""
import re
import bs4
from urllib import parse
import requests
import argparse


def text(input_text: str) -> str:
    params = {"translatetext": input_text}
    target_url = "http://www.gizoogle.net/textilizer.php"
    resp = requests.post(target_url, data=params)
    # the html returned is in poor form normally.
    soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[37].strip("\r\n")  # Hacky, but consistent.
    return giz_text
