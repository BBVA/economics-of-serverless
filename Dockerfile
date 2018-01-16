FROM python:3.6.4

COPY awscosts /usr/lib/python3/awscosts

RUN pip install -e /usr/lib/python3/awscosts

CMD ["python3", "riot.py"]