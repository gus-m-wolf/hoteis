#!/bin/bash

# Remove qualquer instalação anterior
rm -rf .render/chrome

# Cria a pasta e baixa o Chrome
mkdir -p .render/chrome
curl -SL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
dpkg -x chrome.deb .render/chrome/
rm chrome.deb
