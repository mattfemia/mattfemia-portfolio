FROM python:3.8-slim-buster

COPY . /flask-deploy
WORKDIR /flask-deploy
RUN pip install --requirement /flask-deploy/requirements.txt
ENV FLASK_ENV=production
EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info