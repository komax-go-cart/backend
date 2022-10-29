FROM python:3.11.0-alpine3.16
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir templates && \
    cd templates && \
    touch index.html
EXPOSE 80
ENTRYPOINT ["python3", "/app/api/main.py"]