import streamlit as st
import pandas as pd

st.header("Relatório Divpat")
st.text("Exercício 2024")
st.text("Chefe de divisão: Mauro Sergio Barcellos")

# st.set_page_config(layout="wide")

df1 = pd.read_excel('relatorio2024.xlsx',sheet_name=1,decimal=",")
#print(df1)
#print(df1["Valor da Incorporação"])
#print(df1.loc[1])

col1, col2 = st.columns(2)

#-----## funcoes #-----##


def formataTextoNumero(s):

    tam = len(s)
    p1=''
    p2=''
    while (tam>3):

        t=s[-3:]
        t


        tam-=1
        print(ns)

        tam=len(ns)
    return 


#-----## Incorporações #-----## 
### G.Barras

df1_valores=df1.iloc[:-1]
df1_total=df1.tail(1)
# print(df1_valores)
# print(df1_total)



st.subheader("Bens Incorporados")
#st.title("My title")
s=int(df1_total["Bens Incorporados"])
label = str(df1_total["Ano"].iloc[0])
#print(label)


st.subheader(f"Total: {s} bens \n Período: {label}")
#st.title(f"{s}")
#st.text(str(df1_total["Ano"]))

st.subheader("Bens Incorporados x Ano")
st.bar_chart(df1_valores,x="Ano",y="Bens Incorporados")
#st.bar_chart(dtfiltro.sort_values(['Population']),x=["Name","Language"],y="Population")



    



# Quantidade de itens tombados 
# Qtd itens 15079		, data ate 10/12/2024, valor	22078885,48
