#!/bin/bash

locust --headless --only-summary -H http://172.17.2.122 --logfile ./log-locust-$(date +%Y%m%d%H%M) --json

