#!/bin/bash

# cd /app/HTTPServer 
echo "Docker started."
pip install flask
python forever.py &

cd /app/HTTPServer 

python main.py 