from ast import List
import math
from posixpath import split
import socket, sys
from subprocess import call
from threading import Thread
from time import sleep

import plogger

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
        plogger.PepperLogger.log_success("Web Server: " + ip)


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


    def connect_multiple_ips_thread(self, ips, port, callback):
        for ip in ips:
            self.connect_thread(ip, port, callback)


    def split_chunk(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


    def scan_port(self, threads=50):
        if threads > self.ips_range:
            threads = self.ips_range
        #chunks = int(math.floor((self.ips_range / threads)))
        chunked_ips = self.split_chunk(self.ip_list, threads) #[self.ip_list[i:i + chunks] for i in range(0, len(self.ip_list), chunks)]
        for c in chunked_ips:
            thread = Thread(target=self.connect_multiple_ips_thread, args=(c, self.port, self.port_open_callback))
            thread.start()


    def scan_port_with_custom_callback(self, callback, threads=50):
        if threads > self.ips_range:
            threads = self.ips_range
        #chunks = int(math.floor((self.ips_range / threads)))
        chunked_ips = self.split_chunk(self.ip_list, threads) #[self.ip_list[i:i + chunks] for i in range(0, len(self.ip_list), chunks)]
        for c in chunked_ips:
            thread = Thread(target=self.connect_multiple_ips_thread, args=(c, self.port, callback))
            thread.start()


    def scan_single_ip(self, ip, port):
        self.connect_thread(ip, port, self.port_open_callback)

            
    class Wrapper:
        @staticmethod
        def scan_ips(ips, port, threads=50):
            scan = Scanner(ips,port)
            scan.scan_port(threads=threads)


        """@staticmethod
        def scan_single_ip(ip, port):
            scan = Scanner()
            scan.scan_single_ip(ip, port)"""


        @staticmethod
        def scan_ips_with_custom_callback(ips, port, callback, threads=50):
            scan = Scanner(ips, port)
            scan.scan_port_with_custom_callback(callback, threads)
