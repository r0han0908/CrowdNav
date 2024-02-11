FROM starofall/crowdnav

ADD ./ /app/
#ADD ./setup.py /app/setup.py


# COPY . /app 
RUN pip install flask

COPY ./start.sh /app

EXPOSE 3000

WORKDIR /app

RUN chmod 777 ./start.sh

CMD ["bash", "start.sh"]
