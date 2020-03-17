FROM python:3-alpine

WORKDIR /app

RUN apk add --no-cache make 

COPY . /app

RUN make install

ENTRYPOINT [ "myhttpservice" ]