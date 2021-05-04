release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
web: gunicorn api.wsgi
clock: python clock.py