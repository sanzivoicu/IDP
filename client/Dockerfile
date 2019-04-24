FROM python:2.7

EXPOSE 5000

WORKDIR /client

COPY requirements.txt /client
RUN pip install -r requirements.txt

COPY client.py /client

CMD python client.py
