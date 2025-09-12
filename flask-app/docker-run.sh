#! /usr/bin/env bash

docker build -t flask-app .

docker run -d \
    --name flask-app \
    -p 5000:5000 \
    flask-app

