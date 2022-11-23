release: sh -c 'python manage.py migrate && python manage.py loaddata */fixtures/*.json'
web: gunicorn SIREST_B08.wsgi
