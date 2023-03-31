import csv
import json
import multiprocessing
import os
import random
import string
import threading
import time
import requests
import csv
from pathlib import Path
from multiprocessing import Pool, Lock

import pandas as pandas


def generate_data():
    name = ''.join(random.choices(string.ascii_uppercase, k=8))
    device_type = 'sensor'
    frequency = '1Hz'
    kind = 'generic'
    protocol = 'mqtt'
    data_format = 'json'
    producer = 'producer1'
    subnature = 'default'
    static_attributes = '{}'
    service = 'myservice'
    service_path = '/path'
    list_attributes = '{"attr1":"value1", "attr2":"value2"}'
    organization = 'myorg'

    return name, device_type, frequency, kind, protocol, data_format, producer, subnature, static_attributes, \
        service, service_path, list_attributes, organization


def send_request(name, device_type, frequency, kind, protocol, data_format, producer, subnature, static_attributes,
                 service, service_path, list_attributes, organization):
    bc_url = 'http://dashboard:9999/api/adddevice/'
    bc_message = {
        'name': name,
        'type': device_type,
        'frequency': frequency,
        'kind': kind,
        'protocol': protocol,
        'format': data_format,
        'producer': producer,
        'subnature': subnature,
        'static_attributes': static_attributes,
        'service': service,
        'servicePath': service_path,
        'strDev': list_attributes,
        'organization': organization
    }
    headers = {
        'Content-Type': 'application/json'
    }
    start_time = time.time()
    response = requests.post(bc_url, headers=headers, json=bc_message)
    elapsed_time = time.time() - start_time
    status = 'ok' if response.status_code == 200 else 'ko'
    return status, elapsed_time


def log_data(name, device_type, organization, elapsed_time, status):
    with open('device_insertion_result/' + multiprocessing.process.current_process().name + '.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, device_type, organization, elapsed_time, status])


def main(num_devices):
    with open('device_insertion_result/' + multiprocessing.process.current_process().name + '.csv', mode='w') as file:
        writer = csv.writer(file, dialect='excel')
        writer.writerow(['name', 'type', 'organization', 'elapsed_time', 'status'])
    for i in range(num_devices):
        device_data = generate_data()
        name = device_data[0]
        status, elapsed_time = send_request(*device_data)
        log_data(name, 'device' + device_data[1], device_data[12], elapsed_time, status)


if __name__ == "__main__":
    with Pool(12) as p:
        p.map(main, [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

    print("Done!")
