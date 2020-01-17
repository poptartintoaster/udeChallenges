#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]


    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return client_list

def print_stuff(results_list):
    print("IP\t\t\t\tMAC Address\n--------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

scan_results = scan("192.168.132.0/24")
print_stuff(scan_results)
