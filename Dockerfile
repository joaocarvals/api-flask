#Utiliza a imagem do python 3.12 na versão slim
FROM python:3.12-slim

#Define o diretório de trabalho dentro do container
WORKDIR /app

#Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

#Instala todas dependencias do projeto
#--no-cache-dir: Evita que o pip armazene em cache os pacotes instalados, economizando espaço no container.
RUN pip install --no-cache-dir -r requirements.txt

#Copia todos os arquivos do diretório atual para o diretório de trabalho no container
COPY . .

#Informa que a aplicação utilizará a porta 5000
EXPOSE 5000

#Comando executando quando o container for iniciado
#Inicia a aplicação Flask executando o arquivo main.py
CMD ["python", "main.py"]


