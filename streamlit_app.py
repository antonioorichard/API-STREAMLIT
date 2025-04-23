import streamlit as st
import requests
st.set_page_config(
    page_title = "Formulário médico"
    #page_icon = ""

)

api_gateway_endpoint = "https://api-flask-ds.onrender.com/" # Substitua pela URL correta do API Gateway

with st.form( key = 'form1'):
    col1, col2, col3 = st.columns([3,2,1])
    with col1:
            ave_suino  = st.text_input("ave_suino")
    with col2:
            garganta    = st.text_input("garganta")
    with col3:
            perd_pala  = st.text_input("perd_pala")
    with col1:
            febre = st.text_input("febre")
    with col2:
            dispneia   = st.text_input("dispneia")
    with col3:
            diarreia   = st.text_input("diarreia")
    with col1:
            tosse  = st.text_input("tosse")
    with col2:
            perd_olft  = st.text_input("perd_olft")
    with col3:
            vomito     = st.text_input("vomito")
#    st.form_submit_button()
    if st.form_submit_button():
            # Preparar os dados para a chamada do API Gateway
            input_data = {
                    'ave_suino' : ave_suino, 
                    'febre'     : febre,
                    'tosse'     : tosse,
                    'garganta'  : garganta, 
                    'dispneia'  : dispneia, 
                    'perd_olft' : perd_olft,
                    'perd_pala' : perd_pala,
                    'diarreia'  : diarreia, 
                    'vomito'    : vomito 
                   
            }
            # Enviar a requisição POST para o API Gateway
            response = requests.post( api_gateway_endpoint, json = input_data)
    
            # Tratar a resposta do API Gateway 
            if response.status_code == 200:
                # Vamos receber a resposta, do tipo string, então vamos usar .text
                    output_data = response.text
                    st.write("Resultado da inferência: ")
                    st.write( output_data )
            else: 
                    st.write( "Erro ao chamar o API Gateway.")
