FROM python:3
WORKDIR /code
COPY ./fastapi_ms/requirements.txt /code

RUN pip install -r /code/requirements.txt
COPY fastapi_ms /code
EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000", "--reload"]