#! /usr/bin/env bash

docker build -t flask-app .

docker run -d \
    --name flask-app \
    -p 5000:5000 \
    -w  /app
    -v "$(pwd):/app" \ 
    flask-app 
    sh -c 'flask run'

