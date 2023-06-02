import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.realcomm.com/realcomm-2023/program/speakers/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

speaker_data = []

speaker_elements = soup.find_all('div', class_='advisor-person')
# print(speaker_elements )
for speaker_element in speaker_elements:
    speaker_name = speaker_element.find('span', class_='ad-name').text.strip()
    speaker_title = speaker_element.find('span', class_='ad-title').text.strip()

    # Check if the description element exists
    speaker_description_element = speaker_element.find('span', class_='ad-description')
    if speaker_description_element is not None:
        speaker_description = speaker_description_element.text.strip()
    else:
        speaker_description = ""

    speaker_data.append({'Name': speaker_name, 'Title': speaker_title, 'Description': speaker_description})

df = pd.DataFrame(speaker_data)

df.to_excel('speakers_data.xlsx', index=False)
