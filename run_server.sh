#!/bin/sh

IP="192.168.1.32"

export FLASK_APP="server"
#export FLASK_ENV="development"
flask run --host=$IP
