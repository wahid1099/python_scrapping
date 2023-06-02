import pandas as pd
from openpyxl import Workbook

# Create an empty DataFrame to store the data
data = []

# Loop through the pages and extract the required information
for link in page_links:
    page_url = link['href']
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.content, 'html.parser')

    page_name = page_soup.find('h1', class_='page-title').text.strip()
    page_content = page_soup.find('div', class_='content').text.strip()

    data.append({'Page Name': page_name, 'Content': page_content, 'URL': page_url})

# Create a DataFrame from the collected data
df = pd.DataFrame(data)

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Write the DataFrame to the Excel file
for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

# Save the workbook to an Excel file
workbook.save('website_data.xlsx')
