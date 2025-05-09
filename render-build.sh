#!/bin/bash

mkdir -p .render/chrome
curl -SL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
dpkg -x chrome.deb .render/chrome/
rm chrome.deb

mkdir -p .render/chrome/opt/google/chrome
mv .render/chrome/opt/google/chrome/* .render/chrome/opt/google/
