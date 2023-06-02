import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


def extract_web_content(url):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    element = soup.select_one(".main-digies-winners")
    # element = soup.find_all(".main-int")
    

    t = element.get_text().strip()
    lineSpilt = t.splitlines()
    

    def filtered_blank_lines(line):
        return line.strip() != ""

    filtered_lines = list(filter(filtered_blank_lines, lineSpilt))
    data = "\n".join(filtered_lines)
    # data = re.sub(r"\s+", " ", t).strip()

    print(data)
    character_limit = 500
    wb = Workbook()
    ws = wb.active

    num_cells = len(data)

    for i in range(num_cells):
        start_index = i * character_limit
        end_index = (i + 1) * character_limit
        cell_value = data[start_index:end_index]
        ws.cell(row=i + 1, column=1).value = cell_value
    wb.save("Realcomm data.xlsx")

    df = pd.DataFrame(columns=['Home Page'])
    row = [data]
    df.loc[len(df)] = row
    return df


urls = 'https://www.realcomm.com/realcomm-2023/digies/winners/'
extract_web_content(urls)

