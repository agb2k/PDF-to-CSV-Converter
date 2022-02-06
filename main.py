import pdfplumber
import pandas as pd

# Open pdf with pdfplumber
pdf = pdfplumber.open("Q2.pdf")

tableList = []

# Extract table data and append to list
for pages in pdf.pages:
    table = pages.extract_table()
    tableList.append([pages.page_number, table[1][1], table[2][1]])

# Convert to dataframe
df = pd.DataFrame(tableList, columns=['Page Number', 'Description', 'Possible Root Cause'])
df = df.set_index('Page Number')

# Data Cleaning
for column in ["Description", "Possible Root Cause"]:
    df[column] = df[column].str.replace("\n", " ")

# Convert to CSV
df.to_csv('out.csv')
