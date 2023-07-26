FROM alpine:3
LABEL maintainer="brad@foghornconsulting.com"

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache py3-pip curl bash \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

ENV FLASK_APP app.py
RUN mkdir /app
COPY app.py /app

VOLUME /app
EXPOSE 5000

# Cleanup
RUN rm -rf /.wh /root/.cache /var/cache /tmp/requirements.txt

WORKDIR /app
CMD ["/usr/bin/flask", "run", "--reload", "-h", "0.0.0.0"]
