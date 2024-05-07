FROM python:3.10

WORKDIR /storage

COPY /storage/requirements.txt /storage/requirements.txt

RUN pip install -r /storage/requirements.txt

COPY ./storage /storage

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]