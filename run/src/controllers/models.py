#!/usr/bin/env python3
from OpenSSL import crypto
import json
import requests

def get_cert():
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    return True

def get_stats(secret_key, params={}):
    headers = {
        "User-Agent": "bytexmen@mail.com",
        "Content-Type": "application/json"
    }
    params.update(secret=secret_key)
    return requests.get("https://api.coinhive.com/stats/site", params=params, headers=headers).json()

def get_balance(secret_key, params={}):
    headers = {
        "User-Agent": "bytexmen@mail.com",
        "Content-Type": "application/json"
    }
    params.update(secret=secret_key)
    params.update(name="bytexmen@mail.com")
    return requests.get("https://api.coinhive.com/user/balance", params=params, headers=headers).json()
