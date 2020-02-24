FROM python:3.8
COPY ./requirements.txt /flask-app/requirements.txt
RUN pip install -r /flask-app/requirements.txt
COPY ./files_collector /flask-app
EXPOSE 5000/tcp
RUN mkdir -p /home/master/prezentace
RUN mkdir -p /home/master/program_dne
ENV FLASK_APP /flask-app/__init__.py 
CMD flask run --host=0.0.0.0
