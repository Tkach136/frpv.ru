FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /site 
WORKDIR /site
COPY freeze.txt /site/
RUN pip install -r freeze.txt
COPY . /site/
WORKDIR /site/project