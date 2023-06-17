import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realcomm.com/realcomm-2023/program/speakers/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

speaker_data = []

# Find all div elements with the class "advisor-pop"
speaker_elements = soup.find_all('div', class_='advisor-pop')

# Iterate over each speaker element and extract the data
for speaker_element in speaker_elements:
    speaker_name = speaker_element.find('div', class_='ap-name').text.strip()
    speaker_title = speaker_element.find('div', class_='ap-title').text.strip()
    speaker_company = speaker_element.find('div', class_='ap-company').text.strip()

    # Extract session details
    session_times = speaker_element.find_all('div', class_='ap-session-time')
    session_names = speaker_element.find_all('div', class_='ap-session-name')

    session_details = []
    for time, name in zip(session_times, session_names):
        session_time = time.text.strip()
        session_name = name.text.strip()
        session_details.append(f"{session_time}: {session_name}")

    speaker_linkedin_element = speaker_element.find('a', class_='ap-linkedin')
    if speaker_linkedin_element is not None:
        speaker_linkedin = speaker_linkedin_element['href']
    else:
        speaker_linkedin = ""

    speaker_description = speaker_element.find('p').text.strip()

    speaker_data.append({
         'title':'Program Speaker',
         'heading':'Program Speaker'+speaker_name,
         
        'Content':"{}\n{}\n{}\n{}\n{}".format(speaker_name, speaker_title, speaker_company, '\n'.join(session_details), speaker_description),
    })

# Create a DataFrame from the collected data
df = pd.DataFrame(speaker_data)

# Save the DataFrame to an Excel file
df.to_excel('speaker_updateddata2.xlsx', index=False)
