import pandas as pd
import os
# Changing Directory to Project Directory
os.chdir('C:\\Users\\ASUS\\Downloads\\Data\\Data')


df = pd.read_excel("Budget.xlsx",header=3)
df.drop(labels="Grand Total",axis=1,inplace=True)
df.dropna(inplace=True)
df['ProductKey']=df['ProductKey'].astype('int64')

columns=["Category","Sub-Category","ProductName","ProductKey","Month","Budget"]
target = pd.DataFrame(columns=columns)
month=["Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sept","Oct","Nov","Dec"]
records=[]
for i in range(17):
    data=dict()
    for j in range(4):
                data.update({columns[j]:df.iloc[i][j]})
    for k in range(4,16):
                data.update({columns[4]:month[k-4]})
                data.update({columns[5]:df.iloc[i][k]})
                record=data.copy()
                records.append(record)
                record=dict()   
target=target.append(records)
target.to_excel("Budget_modified.xlsx")





