# mini-rag 

This is a minimal implementation of the RAG model for question answering.

## Requirments

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda 
2) Create a new environment
3) Activate the new environment


## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the .env file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update ".env" with your credentials

```bash
$ cd docker
$ sudo docker compose up -d
```

## Run the FASTAPI Server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5001
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets//mini-rag-app.postman_collection.json)

