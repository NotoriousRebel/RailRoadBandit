FROM alpine:latest

RUN apk add --update python3 py3-pip git 

RUN git clone https://github.com/NotoriousRebel/RailRoadBandit

WORKDIR RailroadBandit

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "Bandit.py"]
