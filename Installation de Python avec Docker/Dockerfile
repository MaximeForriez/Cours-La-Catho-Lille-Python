#Dockerfile
#Par défaut, ce fichier installe la dernière version de Python. Pour changer de version, remplacer latest par le numéro de version et sa mineure, comme 3.6, 3.7, 3.8, 3.9, 3.10, 3.11 ou 3.12
FROM python:latest
RUN mkdir /application
WORKDIR "/application"
# Upgrade pip
RUN pip install --upgrade pip
# Update
RUN apt-get update && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /application/
RUN pip install -r /application/requirements.txt
CMD [ "python", "main.py" ]
