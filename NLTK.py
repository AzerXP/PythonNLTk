import nltk.sentiment as nltk
import nltk as nl
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#down = nl.download('vader_lexicon')

def analazir_sentimientos(frase):
    sia = nltk.SentimentIntensityAnalyzer()
    puntacion = sia.polarity_scores(frase)
    if puntacion['neg']  >= 0.2 :
        return'Se siente triste',puntacion['compound'],puntacion['pos'],puntacion['neg']
    
    elif puntacion['pos'] >= 0.2 :
        return'Se siente feliz',puntacion['compound'],puntacion['pos'],puntacion['neg']
    
    else:
        return'Se siente confuso',puntacion['compound'],puntacion['pos'],puntacion['neg']

def  getPuntuacion(frase):
    _ ,puntuacion,_,_ = analazir_sentimientos(frase)
    return puntuacion 

def getEstado(frase):
   estado,_,_,_ = analazir_sentimientos(frase)
   return estado

def guardarPuntuacion(puntuacion):
   puntuacion_actual = 0
   puntuacion_actual += puntuacion
   return puntuacion_actual

 
st.set_page_config(
    page_title="Analisis de Sentimiento",
    layout="wide",#centered
    initial_sidebar_state="expanded",
 )
def entrada_dato(frase):
 boton = st.button("Analizar")
 estado = getEstado(frase)
 puntuacion = getPuntuacion(frase)
 if boton :
    st.text_area("Respuesta de la IA",f"EL estado de animo de la persona es :{estado} y su puntuacion es : {puntuacion}")
   
   
def guardarCantdeEstado(frase):
   contadorFeliz = []
   contadorTriste = []
   contadorConfuso = []
   estado = getEstado(frase)
   if estado == "Se siente feliz":
      contadorFeliz.append("Se siente feliz")
   elif estado == "Se siente triste":
      contadorTriste.append("Se siente Triste")
   else:
      contadorConfuso.append("Se siente Confuso")   
   return contadorFeliz,contadorTriste,contadorConfuso

def mostra_grafico(frase):
   #mostrar = st.button("Mostrar Grafica")
   tipo_grafico = st.selectbox("Graficar",["Grafico de Puntuacion","Mostrar mas datos","cantidad de estado"])
   puntuacion  = getPuntuacion(frase)
   puntuacion_actual = guardarPuntuacion(puntuacion)
   estadoFeliz,estadoTriste,estadoConfuso = guardarCantdeEstado(frase)
   #st.text_area("resultado",f"puntuaciones son : {puntuacion_actual}")
   if tipo_grafico == "Grafico de Puntuacion":
      nombres = ["Puntuación Total"]
      valores = [puntuacion_actual]
      fig, ax = plt.subplots() 
      ax.bar(nombres, valores)
      ax.set_ylabel("Valor")
      ax.set_title("Grafico de Puntuación Total")
      st.pyplot(fig)
   elif tipo_grafico == "Mostrar mas datos":
      nombres = ["Comportamiento","Positividad","Negatividad"]
      _,_,positividad,negatividad = analazir_sentimientos(frase)
      valores = [puntuacion_actual,positividad,negatividad]
      fig, ax  = plt.subplots()
      ax.bar(nombres,valores)
      ax.set_title("Grafico de Info Completa")
      st.pyplot(fig)
   else:
      nombres = ["Cant de Veces Feliz","Cant de Veces Triste","Cant de Veces Confuso"]
      cantFeliz = len(estadoFeliz)
      cantTriste = len(estadoTriste)
      cantConfusa = len(estadoConfuso)
      valores = [cantFeliz,cantTriste,cantConfusa]
      fig , ax = plt.subplots()
      ax.bar(nombres,valores)
      ax.set_xlabel("Estado")
      ax.set_title("Grafico de Estado")
      st.pyplot(fig)
    

st.title("Analisis de Sentimiento")
frase = st.text_input("Ingrese un texto explicando como se siente")
entrada_dato(frase)
mostra_grafico(frase)




 









    