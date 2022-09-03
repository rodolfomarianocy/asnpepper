import socket, sys
from subprocess import call
from threading import Thread
from time import sleep

class Scanner:
    open_ports = {}
    ips_range = -1
    tested_ips = 0

    def __init__(self, ip_list = [], port = 80):
        self.ip_list = ip_list
        self.port = port
        self.ips_range = len(ip_list)


    def port_open_callback(self, ip, port):
        self.open_ports[str(ip)] = port
        print(ip)


    def display_open_ips(self):
        for ip,port in self.open_ports.items():
            print("Porta %s aberta no IP %s" % (port, ip))


    def connect_thread(self, ip, port, callback):
        self.tested_ips = self.tested_ips + 1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect_ex((ip, port))
        if conn == 0:
            callback(ip, port)
        s.close()
        return


    def scan_port(self):
        for ip in self.ip_list:
            thread = Thread(target=self.connect_thread, args=(ip, self.port, self.port_open_callback))
            thread.start()

    def scan_single_ip(self, ip, port):
        self.connect_thread(ip, port, self.port_open_callback)

            
    class Wrapper:
        @staticmethod
        def scan_ips(ips, port):
            scan = Scanner(ips,port)
            scan.scan_port()


        def scan_single_ip(ip, port):
            scan = Scanner()
            scan.scan_single_ip(ip, port)


"""


Scanner.Wrapper.scan_single_ip('10.11.26.112', 80)

ips_test = gen_fake_ips()

scan = Scanner(ips_test, 80)
scan.scan_port()"""
