#!/bin/sh
set -e

myname="$(basename $0)"

msg(){
    echo "$myname: $1"
}

msg "start waiting for database"
./manage.py waitdb

msg "start migrating models"
./manage.py migrate

if ./manage.py diffsettings --all | grep -q "DEBUG = False"; then
    msg "start collecting static files"
    ./manage.py collectstatic --noinput

    msg "start creating administrator"
    ./manage.py initadmin "$DJANGO_ADMIN_PASSWORD"
fi

msg "launching gunicorn"
exec gunicorn --config gunicorn_config.py "$WSGI_APPLICATION"