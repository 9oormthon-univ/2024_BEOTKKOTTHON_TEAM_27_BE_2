FROM python:3.10

WORKDIR /posting

COPY /posting/requirements.txt /posting/requirements.txt

RUN pip install -r /posting/requirements.txt

COPY ./posting /posting

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]