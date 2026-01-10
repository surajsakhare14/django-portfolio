#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
python manage.py create_admin
python manage.py collectstatic --noinput

gunicorn portfolio.wsgi:application
