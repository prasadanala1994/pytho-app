#!/bin/bash
docker pull prasadanala1994/python-app:latest
docker stop pythonapp
docker rm pythonapp
docker run -d --name pythonapp -p 4000:81 prasadanala1994/python-app:latest