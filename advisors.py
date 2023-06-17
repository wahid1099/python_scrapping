
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realcomm.com/realcomm-2023/advisors/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

speaker_data = []

speaker_elements = soup.find_all('div', class_='advisor-pop')
# print(speaker_elements )
for speaker_element in speaker_elements:
    speaker_name = speaker_element.find('div', class_='ap-name').text.strip()
    speaker_title = speaker_element.find('div', class_='ap-title').text.strip()
    speaker_compnay_element = speaker_element.find('div', class_='ap-company')
    session_times = speaker_element.find_all('div', class_='ap-session-time')
    session_names = speaker_element.find_all('div', class_='ap-session-name')

    session_details = []
    for time, name in zip(session_times, session_names):
        session_time = time.text.strip()
        session_name = name.text.strip()
        session_details.append(f"{session_time}: {session_name}")
    # Check if the description element exists
    speaker_description_element = speaker_element.find('p')
    # print(speaker_description_element)
    if speaker_description_element is not None:
        speaker_description = speaker_description_element.text.strip()
    else:
        speaker_description = ""
    if speaker_compnay_element is not None:
        speaker_compnay = speaker_compnay_element.text.strip()
    else:
        speaker_compnay = ""

    # speaker_data.append({
    #      'title':'REALCOMM ADVISORY COUNCIL CO-CHAIRS',
    #      'heading':'REALCOMM ADVISORY COUNCIL CO-CHAIRS'+speaker_name,
         
    #     'Content':"{}\n{}\n{}\n{}".format(speaker_name, speaker_title, speaker_compnay, speaker_description),
    # })
    
    speaker_data.append({
         'name':speaker_name,
         'speaker_title':speaker_title,
         'speaker_compnay_element':speaker_compnay_element,
         'speaker_description':speaker_description,
         'sessions ':"{}\n".join(session_details)
         
    })

df = pd.DataFrame(speaker_data)

df.to_excel('advisors_data13june.xlsx', index=False)
# df.to_csv('speakers_data.txt', sep='\t', index=False)

