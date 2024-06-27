import streamlit as st

import pandas as pd


st.set_page_config(page_title='Meu Site Streamlit')

with st.container():
    st.subheader('Meu primeiro site com streamlit')
    st.title('DashBoard UN09')
    st.write('Informacoes de Manutençao')
    st.write('Quer verificar sua conta? [clique aqui](https://streamlit.io/components?category=all)')

@ st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela  


with st.container():
    st.write('---')
    qtde_dias = st.selectbox('Selecione o periodo', ['7D', '15D', '21D','30D'])
    num_dias = int(qtde_dias.replace('D', ''))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')
    

