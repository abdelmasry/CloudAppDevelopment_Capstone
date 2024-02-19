#!/bin/bash

# Install Python 3.8
sudo apt-get update
sudo apt-get install -y python3.8 python3.8-distutils

# Upgrade pip
/Users/abdelrahmanibrahim/miniconda/bin/python -m pip install --upgrade pip

# Install Cloudant
/Users/abdelrahmanibrahim/miniconda/bin/python -m pip install Cloudant

# Install Flask
/Users/abdelrahmanibrahim/miniconda/bin/python -m pip install Flask
