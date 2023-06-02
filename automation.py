from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook

url = 'https://www.realcomm.com/realcomm-2023/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

page_links = soup.find_all('a', class_='page-link')

data = pd.DataFrame(columns=['Page Name', 'Content', 'URL'])
wb = Workbook()
ws = wb.active

for link in page_links:
    page_url = link['href']
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.content, 'html.parser')

    page_name = page_soup.find('h1', class_='page-title').text.strip()
    page_content = page_soup.find('div', class_='content').text.strip()
    
    data = data.append({'Page Name': page_name, 'Content': page_content, 'URL': page_url}, ignore_index=True)
    ws.value = data
data
data.to_excel('website_data.xlsx', index=False)
