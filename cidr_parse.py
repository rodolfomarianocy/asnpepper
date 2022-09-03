from ipaddress import ip_network, ip_address

class Parse():
    @staticmethod
    def parse_cidr(cidr, do_print=False):
        network = ip_network(cidr)
        if do_print:
            for ip in network:
                print(ip)
        return
