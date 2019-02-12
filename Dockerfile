FROM python:3.6

RUN apt-get update && apt-get install -y openssh-server \
&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps

COPY ./src/requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
