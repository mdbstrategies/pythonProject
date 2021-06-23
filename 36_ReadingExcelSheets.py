import pandas as pd
file = pd.ExcelFile("C:\Users\samoy\PycharmProjects\pythonProject\sales.xlsx")
print(file.sheet_names)