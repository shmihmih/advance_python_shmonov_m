FROM python:3.8.12-slim
#FROM centos:7
#RUN yum install -y https://repo.ius.io/ius-release-el7.rpm
#RUN yum install -y python36u python36-pip python36u-devel

ENV CELERY_BROKER redis://redis:6379/0
ENV CELERY_BACKEND redis://redis:6379/0
ENV MONGO_DB mongodb://localhost:27017/

ENV LC_ALL en_US.utf-8
ENV LANG en_US.utf-8

COPY . /worker
WORKDIR /worker

RUN pip install -r requirements.txt
#ENTRYPOINT ["python3"]
#CMD ["workers.py"]
ENTRYPOINT celery -A workers worker -B --loglevel=info