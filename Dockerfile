#started image for python
FROM python:3.7-alpine

#Set the working directory to /code
WORKDIR /source

#Set environment variables used by the flask command
ENV FLASK_APP=app.py
#set to 0.0.0.0 when want to be reached not only localy
#ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_HOST 127.0.0.1


#Install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

#Copy requirements.txt and install the Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#expose to ports for listening
#HTTP
EXPOSE 8002
#HTTPS
EXPOSE 8003

#Copy the current directory . in the project to the workdir . in the image
COPY . .

#Set the default command for the container to flask run.
CMD ["flask", "run"]