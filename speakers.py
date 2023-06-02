import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.realcomm.com/realcomm-2023/advisors/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

speaker_data = []

# Find all div elements with the class "advisor-pop"
speaker_elements = soup.find_all('div', class_='advisor-pop')
# print(speaker_elements)

# Iterate over each speaker element and extract the data
for speaker_element in speaker_elements:
    speaker_name = speaker_element.find('div', class_='ap-name').text.strip()
    speaker_title = speaker_element.find('div', class_='ap-title').text.strip()
    speaker_company = speaker_element.find('div', class_='ap-company').text.strip()
    # speaker_linkedin = speaker_element.find('a', class_='ap-linkedin')['href'] it dosen't work if the element is null
    speaker_linkedin_element = speaker_element.find('a')
    if speaker_linkedin_element is not None:
        speaker_linkedin = speaker_linkedin_element['href']
    else:
        speaker_linkedin = ""
    speaker_description = speaker_element.find('p').text.strip()
    

    speaker_data.append({
        'Name': speaker_name,
        'Title': speaker_title,
        'Company': speaker_company,
        'LinkedIn': speaker_linkedin,
        'Description': speaker_description,
        
    })

# Create a DataFrame from the collected data
df = pd.DataFrame(speaker_data)

# Save the DataFrame to an Excel file
df.to_excel('advisors.xlsx', index=False)
