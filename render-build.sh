#!/usr/bin/env bash

# Atualizar pacotes e instalar Chromium
apt-get update && apt-get install -y chromium

# Garantir que o Python use os requisitos
pip install -r requirements.txt
