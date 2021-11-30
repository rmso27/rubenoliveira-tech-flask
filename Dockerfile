# Image to be installed
FROM python:3.8-buster

# Create app dir
RUN mkdir -p /usr/src/rubenoliveira-tech-flask

# Copy the app content to the newly created dir
COPY . /usr/src/rubenoliveira-tech-flask

# Start working from the new dir
WORKDIR /usr/src/rubenoliveira-tech-flask

# Setup dependencies
RUN apt update
RUN pip3 install --no-cache-dir -r requirements.txt

# App port
EXPOSE 5000

# Setup ENV VARS
RUN export FLASK_APP=app.py
RUN export FLASK_ENV = production
RUN flask run

# # Start app on boot
# ENTRYPOINT [ "python3.8", "app.py" ]
