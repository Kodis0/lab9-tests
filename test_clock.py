# test_clock.py
import pytest
import requests

def test_api_status():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert res.status_code == 200

def test_api_body_not_empty():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert len(res.json()) > 0
