FROM ubuntu

RUN apt update
RUN apt install python3-pip -y

WORKDIR /app

COPY ./python /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]