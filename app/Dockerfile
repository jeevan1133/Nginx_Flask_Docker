# your code goes here ...
FROM python:3.7-alpine

WORKDIR /var/www/app/

COPY ./src .

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install -r ./requirements.txt

ENTRYPOINT ["python3", "/var/www/app/server.py"]
