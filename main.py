import Datenaufnahme
import pandas as pd


# Alle Zeilen anzeigen
pd.set_option('display.max_rows', 100)

# Alle Spalten anzeigen
pd.set_option('display.max_columns', None)



data = Datenaufnahme.Input()
gemeindeeinwohner = Datenaufnahme.InputEinwohnerzahlen()


data = data[data['Ergebnisse'] != "Parteistimmen"]

print(data.columns)
print(gemeindeeinwohner.columns)

gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['Demografische Komponente'] == "Bestand am 1. Januar"]
gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['Geschlecht'] == 'Geschlecht - Total']
gemeindeeinwohner = gemeindeeinwohner[gemeindeeinwohner['StaatsangehĂśrigkeit (Kategorie)'] == 'StaatsangehĂśrigkeit (Kategorie) - Total']

gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)
gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)
gemeindeeinwohner = gemeindeeinwohner.drop(gemeindeeinwohner.columns[2], axis=1)


gemeindeeinwohner = gemeindeeinwohner.rename(columns={'DATA': 'Einwohner'})
gemeindeeinwohner = gemeindeeinwohner.rename(columns={'Kanton (-) / Bezirk (>>) / Gemeinde (......)': 'Orte'})

data = data.rename(columns={'Bezirk (>>) / Gemeinde (......)': 'Orte'})

#print(gemeindeeinwohner)
#print(data)
#print(data.columns)


print(gemeindeeinwohner)
gemeindeeinwohner['Orte'] = gemeindeeinwohner['Orte'].str.replace(r'\d+', '', regex=True)
gemeindeeinwohner['Orte'] = gemeindeeinwohner['Orte'].str.replace(r'\.\.\.\.\.\. ', '', regex=True)
data['Orte'] = data['Orte'].str.replace(r'\.\.\.\.\.\.', '', regex=True)
#print(gemeindeeinwohner)
print(data)

merged_df = pd.merge(data, gemeindeeinwohner, on=['Orte', 'Jahr'], how='inner')


merged_df = merged_df.replace("\"...\"", 0)
merged_df = merged_df.replace("", 0)


merged_df = merged_df[~merged_df['Orte'].str.startswith('>>')]
#print(merged_df)


file_path = 'output.xlsx'
merged_df.to_excel(file_path, index=False)