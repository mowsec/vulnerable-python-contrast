FROM python:3.9.11-buster

LABEL description="Damn Vulnerable GraphQL Application"
LABEL github="https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application"
LABEL maintainers="Dolev Farhi & Connor McKinnon"

ARG TARGET_FOLDER=/opt/dvga
WORKDIR $TARGET_FOLDER/

RUN apt-get update && apt-get install -y \
        curl \
        autoconf \                      # <-- Contrast Agent dependency
        # ethtool \                       # <-- Contrast Agent dependency ??
        # python3-dev \                   # <-- Contrast Agent dependency
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /opt/dvga/
RUN pip install -r requirements.txt     # <-- Contrast Agent is installed here

ADD core /opt/dvga/core
ADD db /opt/dvga/db
ADD static /opt/dvga/static
ADD templates /opt/dvga/templates

COPY app.py /opt/dvga
COPY config.py /opt/dvga
COPY setup.py /opt/dvga/
COPY version.py /opt/dvga/

RUN python setup.py

EXPOSE 5013/tcp
CMD ["python3", "app.py"]
