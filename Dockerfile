# Image to be installed
FROM python:3.8-buster

# Create app dir
RUN mkdir -p /usr/src/rubenoliveira-tech

# Copy the app content to the newly created dir
COPY . /usr/src/rubenoliveira-tech

# Start working from the new dir
WORKDIR /usr/src/rubenoliveira-tech

# Setup dependencies
RUN apt update
RUN pip3 install --no-cache-dir -r requirements.txt

# App port
EXPOSE 5000

# Start app on boot
ENTRYPOINT [ "python3.8", "app.py" ]
