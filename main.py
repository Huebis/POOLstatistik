import Datenaufnahme
import Datenmanipulation
import pandas as pd
import numpy as np

data = pd.read_excel('output.xlsx', dtype={'Orte': str, 'Jahr': int, 'Partei': str, 'Parteistärke': str, 'DATA': float, 'Einwohner': float})

data = data.drop(data.columns[3], axis=1)

data = data[data["Einwohner"] != 0]


data = data.groupby(['Partei', 'Orte'], as_index=False).agg({
    'DATA': 'mean',  # Berechnet den Durchschnitt
    "Einwohner": 'mean'  # Beibehaltung der ersten Instanz
})






#data = data[data["Jahr"] == 2023]
#data = data[data["DATA"] != 0]


data['Partei'] = data['Partei'].str.replace("CVP","Mitte")


print(data.columns)
print(data.head())


dfSVP = data[data['Partei'] == "SVP"]
dfSP = data[data['Partei'] == "SP"]
dfGrune = data[data['Partei'] == "Grüne"]
dfFDP = data[data['Partei'] == "FDP"]
dfMITTE = data[data['Partei'] == "Mitte"]
dfMITTE = dfMITTE[dfMITTE["DATA"] != 0]

#dfSVP = dfSVP[dfSVP["Jahr"] == 2023]
correlationSVP = dfSVP["DATA"].corr(dfSVP["Einwohner"])
print("Correlation der SVP:")
print(correlationSVP)

dfSP["logEinwohner"] = np.log(dfSP["Einwohner"] + 1e-10)
correlationSP = dfSP["DATA"].corr(dfSP["logEinwohner"])
print("Correlation der SP:")
print(correlationSP)
#print(dfSVP.head())
dfGrune["logEinwohner"] = np.log(dfGrune["Einwohner"] + 1e-10)
correlationGrune = dfGrune["DATA"].corr(dfGrune["logEinwohner"])
print("Correlation der Grünen:")
print(correlationGrune)
print(dfGrune.head())



dfFDP["logEinwohner"] = np.log(dfFDP["Einwohner"] + 1e-10)
correlationFDP = dfFDP["DATA"].corr(dfFDP["logEinwohner"])
print("Correlation der FDP:")
print(correlationFDP)

dfMITTE["logEinwohner"] = np.log(dfMITTE["Einwohner"] + 1e-10)
correlationMITTE = dfMITTE["DATA"].corr(dfMITTE["logEinwohner"])
print("Correlation der MITTE:")
print(correlationMITTE)









#Datenmanipulation.Plotter(dfSVP, "SVP")
dfSVP = dfSVP.sort_values(by='Einwohner', ascending=False).reset_index(drop=True)

dfSVP['Gruppe'] = dfSVP.index // 4
dfSVP = dfSVP.groupby('Gruppe', as_index=False).agg({
    'Einwohner': 'mean',  # Durchschnitt der Einwohner
    'DATA': 'mean'        # Durchschnitt der Data-Werte
})

file_path = 'test.xlsx'
dfSVP.to_excel(file_path, index=False)



print("Korrelation der SVP in einer Exponentialkorrelation")
#dfSVP["logDATA"] = np.log(dfSVP["DATA"]+ 1e-10)
dfSVP["logEinwohner"] = np.log(dfSVP["Einwohner"] + 1e-10)

correlationSVP = dfSVP["DATA"].corr(dfSVP["logEinwohner"])
print("Correlation der SVP aber Exponential:")
print(correlationSVP)


Datenmanipulation.Plotter(dfSVP, "SVP")
Datenmanipulation.Plotter(dfSP, "SP")
Datenmanipulation.Plotter(dfGrune, "Grüne")
Datenmanipulation.Plotter(dfMITTE, "Die Mitte")
Datenmanipulation.Plotter(dfFDP, "FDP")
