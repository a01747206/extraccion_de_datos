import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("datos_facturacion.xlsx")
print(df.head())

filtro1= df[(df["CVE_CLPV"] >= 1000) & (df["CVE_CLPV"]<=2000)]
print(filtro1)
filtro1.to_csv("practica_facturacion_1.csv")

filtro2= df[(df["CVE_VEND"] == 5) & (df["CVE_VEND"]==4)]
print(filtro2)
filtro2.to_csv("practica_facturacion_2.csv")

filtro3=df[df["FECHA_ENT"] == '2022-28-2']
filtro3
filtro3.to_csv("practica_facturacion_3.csv")

filtro4=df[(df["CAN_TOT"] < 5951.7)| (df["STATUS"] == "E")]
filtro4
filtro4.to_csv("practica_facturacion_4.csv")

filtro5 = df.iloc[ : , [0, 6, 7,9]]  
filtro5
filtro5.to_csv("practica_facturacion_5.csv")

filtro6 = df.iloc[7001:7099, :  ] 
filtro6
filtro6.to_csv("practica_facturacion_6.csv")
