FROM python:3.8

USER root

RUN pip install --upgrade pip
RUN apt update

COPY requirements.txt /home
RUN pip install --no-cache-dir -r /home/requirements.txt

COPY save_pretrained_model.py /home
RUN python /home/save_pretrained_model.py

WORKDIR /home

CMD ["echo", "Hello World"]
