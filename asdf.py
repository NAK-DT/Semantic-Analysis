✅ Q1. Simulate Packet Loss
# Q1. Simulate packet loss: Given a list of packet IDs [1,2,3,...], randomly drop 10% and return the rest.
import random

def simulate_packet_loss(packets, loss_rate=0.1):
    kept = [p for p in packets if random.random() > loss_rate]
    return kept

2. Networking Basics
# Example
packets = list(range(1, 101))  # 100 packets
print("Remaining packets after loss:", simulate_packet_loss(packets, 0.1))

# Q2. Write a basic TCP server that listens for messages and echoes them back.
# Use `socket` and handle multiple clients.

# BONUS: Can you simulate network latency using `time.sleep()`?
import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
    conn.close()

def tcp_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server running on {host}:{port}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

# Run with: tcp_server()



3. Multithreading / Concurrency
# Q3. Simulate 10 devices sending data to a server concurrently.
# Use `threading.Thread` or `concurrent.futures.ThreadPoolExecutor`.
import threading
import time
import random

def send_data(device_id):
    for _ in range(5):
        print(f"Device {device_id} sending data: {random.randint(0, 100)}")
        time.sleep(random.uniform(0.2, 0.5))

threads = []
for i in range(10):
    t = threading.Thread(target=send_data, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


4. Testbed Simulator Design
# Q4. Design a class-based simulator for a testbed of devices.
# Each `Device` sends a reading every second. The `TestbedController` gathers all readings.
import time
import random

class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def generate_data(self):
        return {
            "temp": round(random.uniform(20, 60), 2),
            "pressure": round(random.uniform(95, 105), 2)
        }

    def send_data(self, controller):
        data = self.generate_data()
        controller.receive_data(self.device_id, data)

class TestbedController:
    def __init__(self):
        self.data_log = []

    def receive_data(self, device_id, data):
        print(f"Received from {device_id}: {data}")
        self.data_log.append((device_id, data))

# Example use
controller = TestbedController()
devices = [Device(i) for i in range(5)]

for _ in range(3):
    for device in devices:
        device.send_data(controller)
        time.sleep(0.1)


5. Data Parsing / Log Processing
# Q5. Given a log file with JSON lines representing test results, extract failed tests and summarize error messages.
import json

def parse_log(file_path):
    failures = []
    with open(file_path) as f:
        for line in f:
            entry = json.loads(line)
            if entry.get("status") == "fail":
                failures.append(entry)
    return failures

# Example log line:
# {"device_id": 3, "status": "fail", "error": "Timeout"}

# Usage:
# print(parse_log("test_log.json"))



6. Object-Oriented Design
# Q6. Design classes for a `Device`, `Router`, and `Network`. Devices can send messages via Routers.
# Bonus: Add latency and simulate routing decisions.
class Device:
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message, router):
        print(f"[Device {self.device_id}] Sending message: {message}")
        router.route(self.device_id, message)

class Router:
    def __init__(self):
        self.connections = {}

    def connect(self, device):
        self.connections[device.device_id] = device

    def route(self, sender_id, message):
        for did, dev in self.connections.items():
            if did != sender_id:
                print(f"[Router] Routing from {sender_id} to {did}: {message}")

# Example
router = Router()
d1 = Device(1)
d2 = Device(2)
router.connect(d1)
router.connect(d2)

d1.send("Hello, world!", router)




7. Unit Testing
# Q7. Write `unittest` cases for your `Device` class to test its `send_data()` and `connect()` methods.
import unittest

class Device:
    def __init__(self, id):
        self.id = id
        self.connected = False

    def connect(self):
        self.connected = True

    def send_data(self):
        if not self.connected:
            raise Exception("Device not connected")
        return {"status": "ok", "value": 42}

class TestDevice(unittest.TestCase):
    def test_connection(self):
        d = Device(1)
        self.assertFalse(d.connected)
        d.connect()
        self.assertTrue(d.connected)

    def test_send_data_connected(self):
        d = Device(2)
        d.connect()
        result = d.send_data()
        self.assertEqual(result["status"], "ok")

    def test_send_data_unconnected(self):
        d = Device(3)
        with self.assertRaises(Exception):
            d.send_data()

# Run test: unittest.main()




