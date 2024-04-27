import base64
import random

from locust import HttpUser, TaskSet, task
from random import randint, choice


class WebTasks(TaskSet):

    @task
    def load(self):
        tx_id = random.randint(1, 1000000)
        print(f"[start]\ttx_id={tx_id}")
        x = bytes('%s:%s' % ('user', 'password'), 'utf-8')
        base64string = base64.b64encode(x).decode()

        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/login", headers={"Authorization":"Basic %s" % base64string})
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")
        x = random.randint(1, 100)
        if x <= 1.04:
            print(f"[purchace]\t{tx_id}")
            self.client.post("/orders")


class Web(HttpUser):
    tasks = [WebTasks]
    min_wait = 0
    max_wait = 0
