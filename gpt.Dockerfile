FROM python:3.10

WORKDIR /gpt

COPY /gpt/requirements.txt /gpt/requirements.txt

RUN pip install -r /gpt/requirements.txt

COPY ./gpt /gpt

ARG OPENAI_KEY
ARG REST_API_KEY
ARG MAX_TOKENS
ARG TEMPERATURE
ARG TOP_P
ARG N

ENV OPENAI_KEY=$OPENAI_KEY
ENV REST_API_KEY=$REST_API_KEY
ENV MAX_TOKENS=$MAX_TOKENS
ENV TEMPERATURE=$TEMPERATURE
ENV TOP_P=$TOP_P
ENV N=$N

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]