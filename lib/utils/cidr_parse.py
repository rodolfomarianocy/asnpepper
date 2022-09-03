from ipaddress import ip_network, ip_address
import re

class Parse():
    @staticmethod
    def parse_cidr(cidr, do_print=False):
        network = ip_network(cidr)
        if do_print:
            for ip in network:
                print(ip)
        return ip

    @staticmethod
    def extract_cidr_list(cidr_html):
        return re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}', cidr_html)

    @staticmethod
    def extract_org_list(cidr_html):
        return re.findall("(?<=0\/[0-9][0-9]<\/a><\/td><td>)([a-zA-Z,. ]{1,20})(?=<div)", cidr_html)