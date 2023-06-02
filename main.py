from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

def extract_web_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    # tbl = soup.find('table')
    # element = soup.select_one("div",id= 'scholarship')
    element = soup.select_one(".main_int")
    # element = soup.find_all('div', class_='main_int')
    # for div in element:
    # # Extract the element data from each div element
    #  data = div.text.strip()

    t = element.get_text()
    print(t)
    character_limit = 500
    wb = Workbook()
    ws = wb.active

    num_cells = len(t) // character_limit + 1

    for i in range(num_cells):
        start_index = i * character_limit
        end_index = (i + 1) * character_limit
        cell_value = t[start_index:end_index]
        ws.cell(row=i + 1, column=1).value = cell_value
    wb.save("Realcomm_data1.xlsx")


urls = 'https://www.realcomm.com/realcomm-2023/'


extract_web_content(urls)