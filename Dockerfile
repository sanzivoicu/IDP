FROM python:2.7

EXPOSE 5000

WORKDIR /hello

COPY hello.py /hello

CMD python hello.py
