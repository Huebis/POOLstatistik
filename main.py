import Datenaufnahme
import pandas as pd


# Alle Zeilen anzeigen
#pd.set_option('display.max_rows', None)

# Alle Spalten anzeigen
pd.set_option('display.max_columns', None)



data = Datenaufnahme.Input()
gemeindeeinwohner = Datenaufnahme.InputEinwohnerzahlen()
#rint(data.tail(20))
#print("HAHSHSHSHHSSSSSSSSSSS")

#data = data[data['Ergebnisse'] != "Parteistimmen"]
#print(data)
#print(data.head())
#print(data.columns)

#print(data.iloc[100:1044])

print(gemeindeeinwohner.columns)
#print(gemeindeeinwohner.head(30))
#gemeindeeinwohner = gemeindeeinwohner.drop(['Jahr', 'DATA', 'Kanton (-) / Bezirk (>>) / Gemeinde (......)'], axis=1)
gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['Demografische Komponente'] == "Bestand am 1. Januar"]
gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['Geschlecht'] == 'Geschlecht - Total']
gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['StaatsangehĂśrigkeit (Kategorie)'] == 'StaatsangehĂśrigkeit (Kategorie) - Total']

gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)
gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)
gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)

print(gemeindeeinwohner)