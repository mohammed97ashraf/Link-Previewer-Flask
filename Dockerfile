#OS 
FROM python:3.10
RUN apt-get update -y && apt-get install -y build-essential

#coping the code and setPWD to app
COPY ./app /app
WORKDIR /app

#install python libraries 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python","app.py"]
