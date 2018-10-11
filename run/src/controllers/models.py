#!/usr/bin/env python3

import os
import sys
from OpenSSL import crypto

def get_cert():
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    return True

# set up http api so we can check hashes
def get_balance(secret_key):
    https://api.coinhive.com/user/balance

def get_stats(secret_key):
    https://api.coinhive.com/stats/site

