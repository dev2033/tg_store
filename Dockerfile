FROM python:3.8

WORKDIR /Store-bot

COPY requirements.txt /Store-bot/
RUN pip install -r /Store-bot/requirements.txt
COPY . /Store-bot/

CMD python3 /Store-bot/app.py