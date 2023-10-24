# Load / Integration Tests

These tests simulate actual end user usage of the application. They are used to validate the overall functionality and can also be used to put simulated load on the system. The tests are written using [locust.io](http://locust.io)

Run load test:

```
locust --headless --users 10 --spawn-rate 10 -H http://192.0.2.33
```
