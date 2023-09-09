import pandas as pd
excel_file = "附件.xlsx"
df = pd.read_excel(excel_file, sheet_name="Sheet1")


for i in range(1,252):
    for j in range(2,202):
        print(df.iloc[i,j],end='\t')
    print('\n')
