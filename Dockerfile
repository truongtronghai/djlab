FROM ubuntu

RUN apt update && apt install -y python3

RUN apt install -y python3-pip python3-dev default-libmysqlclient-dev build-essential

RUN apt install -y vim

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN django-admin startproject drfapp

WORKDIR /drfapp

RUN cd /drfapp 

EXPOSE 8000/tcp

CMD ["gunicorn","-w 4","-b 0.0.0.0:8000", "--reload","config.wsgi"]
# CMD ["/bin/bash"]
