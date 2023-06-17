import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


def extract_web_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    # element = soup.select_one(".main-int")
    divs = soup.find_all('div', {'class': '.main-int"'})
    data_list = []
    for div in divs:
     data = div.text.strip()  # Extract the text content from the div
     data_list.append(data)



    # t = element.get_text().strip()
    # lineSpilt = t.splitlines()
    

    # def filtered_blank_lines(line):
    #     return line.strip() != ""

    # filtered_lines = list(filter(filtered_blank_lines, lineSpilt))
    # data = "\n".join(filtered_lines)
    # # data = re.sub(r"\s+", " ", t).strip()

    # print(data)
    # character_limit = 35000
    wb = Workbook()
    ws = wb.active

    for i, data in enumerate(data_list, start=1):
     ws.cell(row=i, column=1, value=data)

    wb.save('output.xlsx')


urls = 'https://www.realcomm.com/realcomm-2023/program/'
extract_web_content(urls)

