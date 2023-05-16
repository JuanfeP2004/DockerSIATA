#!/bin/bash

sudo apt update
sudo apt install docker-compose -y
sudo docker build . -f DockerfileFront -t front:v01
sudo docker build . -f DockerfileApi -t api:v01
sudo mkdir ~/volumenSIATA
sudo docker run -d -v ~/volumenSIATA:/datos -p 5000:5000 api:v01
sudo docker run -d -v ~/volumenSIATA:/datos -p 80:80 front:v01
