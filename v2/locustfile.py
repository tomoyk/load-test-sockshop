import base64
import time
import random

from locust import HttpUser, TaskSet, task
from locust import LoadTestShape
from random import randint, choice

import req_sec

# print(sec_req)


class MyCustomShape(LoadTestShape):
    spawn_rate = 1

    def tick(self):
        run_time_sec = self.get_run_time()
        rpmin = req_sec.sec_req.get(run_time_sec // 60 * 60)
        if rpmin is None:
            return (0, spawn_rate)
        elif run_time_sec >= 86400:
            return None

        rps = rpmin // 60
        return (rpmin, spawn_rate)


class WebTasks(TaskSet):

    @task
    def load(self):
        tx_id = random.randint(1, 1000000)
        # print(f"[start]\ttx_id={tx_id}")
        x = bytes("%s:%s" % ("user", "password"), "utf-8")
        base64string = base64.b64encode(x).decode()

        try:
            catalogue = self.client.get("/catalogue").json()
            category_item = choice(catalogue)
        except KeyError:
            time.sleep(3)
            catalogue = self.client.get("/catalogue").json()
            category_item = choice(catalogue)

        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/login", headers={"Authorization": "Basic %s" % base64string})
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))

        # Add cart: 11618 / 442219
        x = random.randint(1, 100)
        if x <= 2.62:
            self.client.delete("/cart")
            self.client.post("/cart", json={"id": item_id, "quantity": 1})
            self.client.get("/basket.html")
        else:
            return

        # Order: 4621 / 11618
        x = random.randint(1, 100)
        if x <= 39.77:
            # print(f"[purchace]\t{tx_id}")
            self.client.post("/orders")


class Web(HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0
