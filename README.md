# Python with RabbitMQ

[![License][license-badge]][license-url]

> A playground for Python and RabbitMQ.

# Installation

## Windows Installation

* Install Erlang : [otp_win64_20.0.exe](http://erlang.org/download/otp_win64_20.0.exe)

* Install RabbitMQ: [rabbitmq-server-3.6.12.exe](https://github.com/rabbitmq/rabbitmq-server/releases/download/rabbitmq_v3_6_12/rabbitmq-server-3.6.12.exe)

* Install Python3: [python-3.5.2-amd64.exe](https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe)

* Install `pika`

```bash
$ pip install pika==0.11.0
```

## Enable RabbitMQ Management Plugin (optional)

```bash
$ cd C:\Program Files\RabbitMQ Server\rabbitmq_server-3.6.12\sbin
$ rabbitmq-plugins enable rabbitmq_management
```

Browser to: [http://localhost:15672](http://localhost:15672)

* Username: guest
* Password: guest

# Development

* Cloning the repo

```bash
$ git clone https://github.com/robertoachar/python-rabbitmq.git
```

# Usage

* Hello World

```bash
# producer
$ python hello-world/producer.py

# consumer
$ python hello-world/consumer.py
```

* Work Queues

```bash
# task
$ python work-queues/task.py

# worker
$ python work-queues/worker.py
```

# Troubleshooting

## Installing as a non-administrator user leaves .erlang.cookie in the wrong place

This makes it impossible to use `rabbitmqctl`.

Workarounds:

* Run the installer as an administrator _or_;
* Copy the file `.erlang.cookie` manually from `%SystemRoot%` to `%HOMEDRIVE%%HOMEPATH%`.
* Restart service (stop and start)

# Author

[Roberto Achar](https://twitter.com/robertoachar)

# License

[MIT](https://github.com/robertoachar/node-rabbitmq/blob/master/LICENSE)

[license-badge]: https://img.shields.io/github/license/robertoachar/node-rabbitmq.svg
[license-url]: https://opensource.org/licenses/MIT
