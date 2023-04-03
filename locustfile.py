import csv
import random
import string
import pandas as pd
from pathlib import Path

from locust import HttpUser, task, between, FastHttpUser

i = 0
path_to_data = Path(r'C:\Users\branchi\PycharmProjects\pythonProject\device_insertion_result\insertion.csv')


class MyUser(FastHttpUser):
    wait_time = between(1, 3)

    # @task
    # def test_add_device(self):
    #     global i
    #     device_data = {
    #         "name": "device" + str(i),
    #         # "name":  "".join(random.choices(string.ascii_uppercase, k=8)),
    #         "type": "TestType",
    #         "frequency": "TestFrequency",
    #         "kind": "TestKind",
    #         "protocol": "TestProtocol",
    #         "format": "TestFormat",
    #         "producer": "TestProducer",
    #         "subnature": "TestSubnature",
    #         "static_attributes": "{\"attr1\": \"Test Attr 1\", \"attr2\": \"Test Attr 2\"}",
    #         "service": "TestService",
    #         "servicePath": "TestServicePath",
    #         "strDev": "TestStrDev",
    #         "organization": "TestOrganization"
    #     }
    #     i = i + 1
    #     with open('device_insertion_result/insertion.csv', mode='a',
    #               newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([device_data['name'], 'device', device_data['type'], device_data['organization']])
    #
    #     with self.client.post("/api/adddevice/", json=device_data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure(f"Got status code {response.status_code}")

    @task
    def test_query_device(self):
        global i
        device_data = {
            "name": "device" + str(i),
            "type": "TestType",
            "organization": "TestOrganization"
        }
        i=i+1
        with self.client.post("/api/deviceVerificationCheck/", json=device_data, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Got status code {response.status_code}")

    # @task
    # def test_add_model(self):
    #     device_data = {
    #         "name": "".join(random.choices(string.ascii_uppercase, k=8)),
    #         "type": "TestType",
    #         "frequency": "TestFrequency",
    #         "kind": "TestKind",
    #         "protocol": "TestProtocol",
    #         "format": "TestFormat",
    #         "producer": "TestProducer",
    #         "subnature": "TestSubnature",
    #         "static_attributes": "{\"attr1\": \"Test Attr 1\", \"attr2\": \"Test Attr 2\"}",
    #         "service": "TestService",
    #         "servicePath": "TestServicePath",
    #         "strDev": "TestStrDev",
    #         "organization": "TestOrganization"
    #     }
    #     with open('device_insertion_result/insertion_model.csv', mode='a',
    #               newline='') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([device_data['name'], 'model', device_data['type'], device_data['organization']])
    #
    #     with self.client.post("/api/addmodel/", json=device_data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure(f"Got status code {response.status_code}")
    #
    # @task
    # def test_query_model(self):
    #
    #     with open('device_insertion_result/insertion_model.csv') as csv_file:
    #         csv_reader = csv.reader(csv_file)
    #         rows = list(csv_reader)
    #         row=rows.pop(random.randint(1, len(rows)-1))
    #
    #         device_data = {
    #             "name": row[0],
    #             "type": row[2],
    #             "organization": row[3]
    #         }
    #         print(device_data)
    #
    #
    #
    #     with self.client.post("/api/modelVerificationCheck/", json=device_data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure(f"Got status code {response.status_code}")
