FROM python:3.10

WORKDIR /posting

COPY /posting/requirements.txt /posting/requirements.txt

RUN pip install -r /posting/requirements.txt

COPY ./posting /posting

ARG BASE_URL
ARG GPT_PORT
ARG POSTING_PORT
ARG STORAGE_PORT
ARG KOGPT_API
ARG CHATGPT_API

ENV BASE_URL=$BASE_URL
ENV GPT_PORT=$GPT_PORT
ENV POSTING_PORT=$POSTING_PORT
ENV STORAGE_PORT=$STORAGE_PORT
ENV KOGPT_API=$KOGPT_API
ENV CHATGPT_API=$CHATGPT_API

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]