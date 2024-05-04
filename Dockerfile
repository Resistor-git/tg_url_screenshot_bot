FROM python:3.12
LABEL authors="Resistor"
WORKDIR /app
COPY . /app

RUN pip install pip --upgrade
RUN pip install -r requirements.txt --no-cache-dir

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

CMD ["python3", "main.py"]
