import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.realcomm.com/realcomm-2023/exhibitors/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')




data = []

for tag in soup.find_all(['div', 'p', 'a']):
    text = tag.get_text(strip=True)
    if text:
        data.append(text)

df = pd.DataFrame({'Data': data})

df.to_excel('data.xlsx', index=False)