import Datenaufnahme
import pandas as pd
import matplotlib.pyplot as plt

def main():
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
    merged_df['Partei'] = merged_df['Partei'].str.replace('')
    #print(merged_df)


    file_path = 'output.xlsx'
    merged_df.to_excel(file_path, index=False)


def Plotter(df,Partei):

    plt.figure(figsize=(8, 6))  # Festlegen der Größe des Diagramms
    plt.scatter(df["logEinwohner"], df["DATA"], color='blue', alpha=0.7, label='Datenpunkte')

    # Achsentitel und Titel setzen
    plt.title(Partei + " in Relation zu den Einwohnerzahlen", fontsize=14)
    plt.xlabel('Einwohnerzahlen', fontsize=12)
    plt.ylabel('Relative Parteistimmen', fontsize=12)

    # Legende und Gitter hinzufügen
    plt.legend()
    plt.grid(True)

    # Diagramm anzeigen
    plt.show()
    plt.savefig(Partei + ".png")
