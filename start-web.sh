#!/bin/bash

python3 quotes/manage.py migrate

python3 quotes/manage.py runserver 0.0.0.0:8000