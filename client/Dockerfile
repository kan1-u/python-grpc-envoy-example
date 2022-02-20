FROM python:3.9-bullseye

RUN apt-get update

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 install -r /tmp/pip-tmp/requirements.txt

COPY src/ /app/

ENTRYPOINT ["python", "/app/app.py"]
