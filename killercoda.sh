#!/bin/bash

# Install dependencies
sudo apt-get update -y
sudo apt-get install -y git python3 python3-pip

# Clone repo
git clone https://github.com/RafaelFino/learn-ops-content.git
cd learn-ops-content

# Install Python packages
pip3 install -r requirements.txt

# Run the application
cd src
python3 start.py