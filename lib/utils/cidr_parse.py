from ipaddress import ip_network
import re

class Parse():
    @staticmethod
    def parse_cidr(cidr, do_print=False):
        network = ip_network(cidr)
        if do_print:
            for ip in network:
                print(ip)
        return network

    @staticmethod
    def extract_cidr_list(cidr_html):
        return re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}', cidr_html)

    @staticmethod
    def extract_org_list(cidr_html):
        return re.findall("(?<=0\/[0-9][0-9]<\/a><\/td><td>)([0-9a-zA-Z,. -\/()\\~_@¨]+)(?=<div)", cidr_html)
    
    @staticmethod
    def input_thread(input_list):
        list = []
        with open(input_list) as file:
            for orgtwo in file:
                list.append(orgtwo.replace("\n",""))
        return list