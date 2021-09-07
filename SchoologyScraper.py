#!/usr/bin/env python3
import re
from urllib.request import urlopen

url = "https://app.schoology.com/calendar/72597028/2021-09"
webpage = urlopen(url)
html_bytes = webpage.read()
html = html_bytes.decode("utf-8")
print(html)
    