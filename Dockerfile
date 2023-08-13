FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3.8-dev \
    python3.8-distutils \
    python3-pip \
    make \
    wget \
    ffmpeg \
    libsm6 \
    libxext6 \
    curl \
    vim
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
#RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.8 get-pip.py

WORKDIR /planet_service

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

#RUN make download_weights_docker

EXPOSE 5000

CMD make run_app_docker
