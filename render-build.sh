#!/usr/bin/env bash

# Instalar Chromium
apt-get update && apt-get install -y chromium

# Descobrir o caminho real do executável
which chromium || which chromium-browser || echo "Chromium não encontrado"

# Garantir instalação dos requisitos Python
pip install -r requirements.txt
