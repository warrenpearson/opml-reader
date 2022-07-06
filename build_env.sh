#!/bin/bash

rm -rf venv

pyenv global 3.9.6
python3 -m venv venv

source venv/bin/activate

python3 -m pip install --upgrade pip
pip3 install -r requirements.txt 
