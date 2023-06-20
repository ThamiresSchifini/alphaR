# Django project
### This is a project about the solar system of alphaR star. Here is possible to list, create, edit and delete planets. It's possible to add all the chemical elements, percentage of water, probability of life, and the alphaR distance to the planet.

## Install requirements
- docker and docker-compose
- python 3.10.6

## Instalation
- git clone https://github.com/ThamiresSchifini/alphaR.git
- create and activate a virtual env
    - venv myenv
    - source myenv/bin/activate
- Install dependencies
    - python3 -m pip install -r requirements.txt
- Execute the migrations
    - python3 manage.py makemigrations
    - python3 manage.py migrate

## Run with docker
- docker build -f Dockerfile -t alpha-r .
- docker run -p 8000:8000 alpha-r

## Run with server
- python manage.py runserver