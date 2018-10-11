#!/usr/bin/env python3

import os
import sys
from OpenSSL import crypto
import json
import requests

def get_cert():
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    return True

def get_stats(secret_key):
    headers = {
        "User-Agent": "ByteXmen@mail.com",
        "Content-Type": "application/json"
    }
    return requests.get("https://api.coinhive.com/stats/site", secret_key, headers).json()

def get_balance(secret_key):
    headers = {
        "User-Agent": "ByteXmen@mail.com",
        "Content-Type": "application/json"
    }
    return requests.get("https://api.coinhive.com/user/balance", secret_key, headers).json()
