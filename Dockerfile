# python:alpine is 3.{latest}
FROM python:alpine
LABEL maintainer='Andre Ferreira'
COPY requirements.txt app.py ./
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "app.py"]
