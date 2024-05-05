FROM python:3.10

WORKDIR /gpt

COPY /gpt/requirements.txt /gpt/requirements.txt

RUN pip install -r /gpt/requirements.txt

COPY ./gpt /gpt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]