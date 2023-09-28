FROM python:3.8-slim-buster

ENV FLASK_APP=front-qa
ENV FLASK_RUN_PORT=5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000