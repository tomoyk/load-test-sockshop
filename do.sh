#!/bin/bash

locust --headless --users 4 --spawn-rate 3.344 --only-summary -H http://172.17.2.122
