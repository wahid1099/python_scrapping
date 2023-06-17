import requests
from bs4 import BeautifulSoup

url = "https://www.realcomm.com/realcomm-2023/program/speakers/"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

speaker_data = []

speaker_elements = soup.find_all('div', class_='advisor-pop')

for speaker_element in speaker_elements:
    speaker_name = speaker_element.find('div', class_='ap-name').text.strip()
    speaker_title = speaker_element.find('div', class_='ap-title').text.strip()
    speaker_company_element = speaker_element.find('div', class_='ap-company')
    session_times = speaker_element.find_all('div', class_='ap-session-time')
    session_names = speaker_element.find_all('div', class_='ap-session-name')
    print(session_names)

    session_details = []
    for time, name in zip(session_times, session_names):

        session_time = time.text.strip()
        session_name = name.text.strip()

        session_details.append(f"{session_time}: {session_name}")

    speaker_description_element = speaker_element.find('p')
    if speaker_description_element is not None:
        speaker_description = speaker_description_element.text.strip()
    else:
        speaker_description = ""
    if speaker_company_element is not None:
        speaker_company = speaker_company_element.text.strip()
    else:
        speaker_company = ""
        

    speaker_data.append({
        'Name': speaker_name,
        'Title': speaker_title,
        'Company': speaker_company,
        'Description': speaker_description,
        'Sessions': "\n".join(session_details)
    })

# Save the data to a text file

with open('speakers_data.txt', 'w') as file:
    for speaker in speaker_data:
        file.write("Name: " + speaker['Name'] + "\n")
        file.write("Title: " + speaker['Title'] + "\n")
        file.write("Company: " + speaker['Company'] + "\n")
        file.write("Description: " + speaker['Description'] + "\n")
        file.write("Sessions: " + speaker['Sessions'] + "\n")
        file.write("\n")
