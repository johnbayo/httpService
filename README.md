# httpservice
This repository contains the code for the httpservice challenge. It is deployed in my gitlab registry which is accessible publicly

## Requirements

Tested with python version `3.5.2 linux/amd64`
or
Docker installed locally

## License

See `LICENSE`

## Copyright

(c) John O. Adebayo 2020

## Usage

``` bash
~$ docker run -it registry.gitlab.com/john.bayo/httpservice/httpservice -h
usage: myhttpservice [-h] [-p PORT]
optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --PORT PORT
```

## Endpoints Usage

``` bash
~$ docker run -p 80:8080 -it registry.gitlab.com/john.bayo/httpservice/httpservice
Server UP at :8080
server up
2020-03-29 12:02:02,588 [INFO] 172.17.0.1 - - [29/Mar/2020 12:02:02] "GET /helloworld HTTP/1.1" 200 -
2020-03-29 12:04:32,951 [INFO] 172.17.0.1 - - [29/Mar/2020 12:04:32] "GET /helloworld?name=OluwasegunJohnAdebayo HTTP/1.1" 200 -
2020-03-29 12:06:37,858 [INFO] 172.17.0.1 - - [29/Mar/2020 12:06:37] "GET /versionz HTTP/1.1" 200 -
```

## Endpoints

`/helloworld --> Hello Stranger`

`/helloworld?name=OluwasegunJohnAdebayo --> Oluwasegun John Adebayo`

`/versionz --> {"name":"httpservice", "version":"0.01"}`