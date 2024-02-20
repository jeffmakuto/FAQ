FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN pip3 install Werkzeug==2.0.2

RUN pip3 install gunicorn==20.1.0

RUN pip3 install spacy==3.7.4

RUN python3 -m spacy download en_core_web_sm

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
