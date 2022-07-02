FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install gunicorn

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000
CMD  ["gunicorn", "-b", ":8000", "-w", "1", "tvshowratinganalyzer.wsgi:application"]