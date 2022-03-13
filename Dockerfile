FROM debian

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y pip

RUN pip3 install sndfile
RUN pip3 install soundfile
RUN pip3 install pedalboard

WORKDIR /cpbox
