# Criando o app/Dockerfile
FROM python:3.12-slim
# Escolheno a versão do python

WORKDIR /app
#criando uma pasta chamada app/ É um diretório de trabalho

COPY . /app
# Copiando tudo que tenho localmente para o contâiner

#RUN apt-get update && apt-get install -y \ 
#    build-essential \
#    curl \
#    software-properties-common \
#    git \ 
#    && git clone https//github.com/endereço do github
# COmando anterior é instalando o git e clona o arquivos que estão no repositório remoto
# arquivos este como arquivo streamlit_app.py e requirements.txt

RUN pip3 install -r requirements.txt
# Intalando as dependências necessárias

EXPOSE 8501
# Específica qual porta o container vai escutar. 8501 é uma porta padrão do Streamlit.

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# o container por sí só executa a aplicação ao ser executado

#CMD ["streamlit", "run", "--server.port", "8501", "streamlit_app.py"]

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
