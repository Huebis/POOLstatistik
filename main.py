import Datenaufnahme
import pandas as pd


data = Datenaufnahme.Input()

print(data.tail(20))
print("HAHSHSHSHHSSSSSSSSSSS")

data = data[data['Ergebnisse'] != "Parteistimmen"]
print(data)
print(data.head())
print(data.columns)

print(data.iloc[100:1044])