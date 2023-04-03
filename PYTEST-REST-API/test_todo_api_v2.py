import requests

ENDPOINT = "http://1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL@164.92.218.36:8080/api/currencies"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    print(response)


def test_can_call_endpoint_v2():
    response = requests.put(ENDPOINT)
    print(response)


def test_can_call_endpoint_v3():
    response = requests.post(ENDPOINT)
    print(response)


def test_can_call_endpoint_v4():
    response = requests.delete(ENDPOINT)
    print(response)


def test_can_call_endpoint_v5():
    response = requests.head(ENDPOINT)
    print(response)
