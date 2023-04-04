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

    # @task
    # def test_query_device(self):
    #     global i
    #     device_data = {
    #         "name": "device" + str(i),
    #         "type": "TestType",
    #         "organization": "TestOrganization"
    #     }
    #     i = i + 1
    #     with self.client.post("/api/deviceVerificationCheck/", json=device_data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure(f"Got status code {response.status_code}")
    #
    # @task
    # def test_add_model(self):
    #     global i
    #     device_data = {
    #         "name": "model" + str(i),
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
    #     global i
    #     device_data = {
    #         "name": "model" + str(i),
    #         "type": "TestType",
    #         "organization": "TestOrganization"
    #     }
    #     i = i + 1
    #     with self.client.post("/api/modelVerificationCheck/", json=device_data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #             response.failure(f"Got status code {response.status_code}")

    @task
    # def test_data_insertion(self):
    #     global i
    #     data = {
    #         "devName": "dati"+str(i),
    #         "devType": "ServiceURI",
    #         "strDev": '{"humidity":{"value":"40"},"temp":{"value":"20"}}',
    #         "organization": "TestOrganization"
    #     }
    #     i=i+1
    #     with self.client.post("/api/adddata/", json=data, catch_response=True) as response:
    #         if response.status_code == 200:
    #             response.success()
    #         else:
    #
    #             response.failure(f"Got status code {response.status_code}")

    @task
    def test_data_query(self):
        #TODO NON FA
        global i
        data = {
            "name": "dati" + str(i),
            "bindings": '{"humidity":{"value":"40"},"temp":{"value":"20"},"dateObserved":{"value":"1970-01-01T00:00:00.000Z"}}',
            "organization": "TestOrganization"
        }
        i = i + 1
        with self.client.post("/api/dataCertificationCheck/", json=data, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:

                response.failure(f"Got status code {response.status_code}")