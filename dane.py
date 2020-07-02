import pandas as pd

lista = [
{'id':'2137', 'imie':'Jan', 'nazwisko':'Nowak'},
{'id':'3333', 'imie':'Robi', 'nazwisko':'Nierobi'},
{'id':'1212', 'imie':'Kot', 'nazwisko':'Rudy'},
{'id':'7777', 'imie':'Intel', 'nazwisko':'Core'}]

lista.sort(key=lambda x: x['nazwisko'])

labels=['id', 'imie', 'nazwisko']
df1=pd.DataFrame.from_records(lista,columns=labels)
df1

print(df1)