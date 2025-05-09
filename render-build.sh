#!/usr/bin/env bash

# Instalar dependências do Chrome
apt-get update && apt-get install -y wget gnupg unzip curl

# Baixar e instalar o Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb

# Rodar o build padrão (ajuste conforme necessário)
pip install -r requirements.txt
