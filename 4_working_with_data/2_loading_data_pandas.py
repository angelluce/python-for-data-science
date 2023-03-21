import pandas as pd

csv_path = '../resources/ChecoPerez.csv'
xlsx_path = '../resources/F1.xlsx'

df1 = pd.read_csv(csv_path)
df2 = pd.read_excel(xlsx_path)

#print(df1)
#print(df2)

dfT = df2[['Año', 'Gran Premio']]

#print(dfT)

dfA = df2['Año'].unique()

#print(dfA)

dfB = df2[df2['Año'] >= 2020]

#dfB.to_csv('../resources/demo.csv')

print(df2.iloc[0,2])