FROM alpine:3
LABEL maintainer="brad@foghornconsulting.com"

RUN apk add --no-cache postgresql-client bash

RUN mkdir /app
COPY db-init.sh /app
COPY create.sql /app

VOLUME /app

# Cleanup
RUN rm -rf /.wh /root/.cache /var/cache

WORKDIR /app
CMD ["/app/db-init.sh"]
