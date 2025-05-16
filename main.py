import Datenaufnahme
import Datenmanipulation
import pandas as pd
import numpy as np

data = pd.read_excel('output.xlsx', dtype={'Orte': str, 'Jahr': int, 'Partei': str, 'Parteistärke': str, 'DATA': float, 'Einwohner': int})

data = data.drop(data.columns[3], axis=1)

data = data[data["Einwohner"] != 0]



print(data.columns)
print(data.head())


dfSVP = data[data['Partei'] == "SVP"]
dfSP = data[data['Partei'] == "SP"]
dfGrune = data[data['Partei'] == "Grüne"]

dfSVP = dfSVP[dfSVP["Jahr"] == 2023]
correlationSVP = dfSVP["DATA"].corr(dfSVP["Einwohner"])
print("Correlation der SVP:")
print(correlationSVP)


correlationSP = dfSP["DATA"].corr(dfSP["Einwohner"])
print("Correlation der SP:")
print(correlationSP)
#print(dfSVP.head())

correlationGrune = dfGrune["DATA"].corr(dfGrune["Einwohner"])
print("Correlation der Grünen:")
print(correlationGrune)
print(dfGrune.head())


#Datenmanipulation.Plotter(dfSVP, "SVP")



print("Korrelation der SVP in einer Exponentialkorrelation")
#dfSVP["logDATA"] = np.log(dfSVP["DATA"]+ 1e-10)
dfSVP["logEinwohner"] = np.log(dfSVP["Einwohner"] + 1e-10)

correlationSVP = dfSVP["DATA"].corr(dfSVP["logEinwohner"])
print("Correlation der SVP aber Exponential:")
print(correlationSVP)


Datenmanipulation.Plotter(dfSVP, "SVP")