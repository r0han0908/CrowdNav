FROM python:2.7

ADD  /app/HTTPServer /app/HTTPServer
COPY  /app/simulation /app/simulation
COPY knobs.json knobs.json

# WORKDIR /app

# COPY . /app 
RUN pip install flask

# WORKDIR /app
RUN chmod +x start.sh
CMD [ "start.sh"  ] 
