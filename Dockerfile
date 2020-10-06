FROM python:3.8.6-alpine as install
RUN apk add --update --no-cache uwsgi uwsgi-python3
COPY ./requirements.txt /flask-app/requirements.txt
RUN pip install -r /flask-app/requirements.txt
COPY ./files_collector /flask-app
RUN mkdir -p /home/master/prezentace
RUN mkdir -p /home/master/program_dne
ENV FLASK_APP /flask-app/__init__.py 

FROM install as dev
CMD flask run --host=0.0.0.0

FROM install as prod
CMD ["gunicorn", "-b", "0.0.0.0", "flask-app.app:app" ]
