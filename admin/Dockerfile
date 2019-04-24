FROM python:3.6

EXPOSE 5000

WORKDIR /admin

COPY requirements.txt /admin
RUN pip install -r requirements.txt

COPY wait-for-it.sh /admin
COPY admin.py /admin
CMD python admin.py
