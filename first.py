import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.realcomm.com/realcomm-2023/register/')
 
print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='main-int')
content = s.find_all('p')

# for link in soup.find_all('a'):
    # print(link.get('href'))
    # pass

images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)

 