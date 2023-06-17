import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.realcomm.com/realcomm-2023/exhibitors/"

with open('html_content.txt', 'r') as file:
    html_content = file.read()

# response = requests.get(url)
# html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

booth_no = []

href_list = []
img_src_list = []
data = []
main_div = soup.find('div', class_='webinar-sponsors')
divs = main_div.find_all('div')

# print(speaker_elements)
for div in divs:
    
    a_element = div.find('a')
    booth_number = div.find('span').text.strip()

    href = a_element['href']
    img_element =div.find('img')['src']
    data.append((href, img_element, booth_number))
    
df = pd.DataFrame(data, columns=['Href', 'Img Src', 'Booth Number'])

df.to_excel('sponserdata.xlsx', index=False)
    
   