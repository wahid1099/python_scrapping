import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


def extract_web_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    # tbl = soup.find('table')
    element = soup.select_one(".main-int")

    # element = soup.select_one("div",id= 'scholarship')


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
    wb.save("Realcomm_data.xlsx")
    # print(t)
    # Print the contents of all selected elements
    # for element in elements:
    #     print(element.text)
    # Print the contents of all selected elements
    # t = element.get_text().find('elements')
    # t = soup.find_all('element')
    headings = soup.find_all('h2')
    paragraphs = soup.find_all('p')
    spans = soup.find_all('span')
    links = soup.find_all('a')
    df = pd.DataFrame(columns=['Home Page'])
    row = []
    row.append(t)
    # for i in range(max(len(headings), len(paragraphs), len(spans), len(links))):
    #     row = []
    #     if i < len(headings):
    #         row.append(headings[i].text.strip())
    #     else:
    #         row.append('')
    #     if i < len(paragraphs):
    #         row.append(paragraphs[i].text.strip())
    #     else:
    #         row.append('')
    #     if i < len(spans):
    #         row.append(spans[i].text.strip())
    #     else:
    #         row.append('')
    #     if i < len(links):
    #         row.append(links[i].get('href'))
    #     else:
    #         row.append('')
    df.loc[len(df)] = row
    return df

urls = ['https://www.realcomm.com/realcomm-2023/attendees/group-sales/']








writer = pd.ExcelWriter('Realcomm Web Scrapping Data 2.xlsx', engine='xlsxwriter')

for i, url in enumerate(urls):
    df = extract_web_content(url)
    df.to_excel(writer, index=False)

    # data save

