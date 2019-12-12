FROM debian:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev libpq-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt    

COPY BuildOptions.py /usr/src/app/
COPY ByThread.py /usr/src/app/
COPY Crud.py /usr/src/app/
COPY EightQueens.py /usr/src/app/
COPY Model.py /usr/src/app/
COPY Service.py /usr/src/app/
COPY test.py /usr/src/app/
COPY Utils.py /usr/src/app/

CMD ["python", "/usr/src/app/EightQueens.py", "8"]