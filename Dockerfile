FROM python:3.11-slim-buster #download docker image which is python 3.11 version

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]


