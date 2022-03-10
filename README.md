# Overview

This example shows how to use OpenTelemetry's API to create, augment, and report spans. The goal is for us to be able to create spans and ultimately see them in the Lightstep UI. 

## Setup

* * *

* You will need Python 3 installed
* You will need pip3 installed
* You will need to run:
```
	pip3 install opentelemetry-api
	pip3 install opentelemetry-sdk
	pip3 install opentelemetry-exporter-otlp
```

## Run the Application

* * *

1. Run the program:
```
	python bubbleSort.py
```

You should see traces exported to your console and your instance of Lightstep if you appropriately configured your access token.

## Useful Links

* * *
* OpenTelemetry: https://github.com/open-telemetry/opentelemetry-python/

## License

* * *
Apache License 2.0