#!/usr/bin/python3

from argparse import RawTextHelpFormatter
from operator import ne
import re, argparse, sys

### include lib/utils, lib/tests ###
sys.path.insert(1, 'lib/utils')
sys.path.insert(1, 'lib/tests')
#####################################

import cidr_parse, cidr_getter, git_scanner, port_scan, file_manager, plogger


def main(org,name):
    cidr_html = cidr_getter.Getter.get_bgp(org)
    cidr_list = cidr_parse.Parse.extract_cidr_list(cidr_html)
    org_list = cidr_parse.Parse.extract_org_list(cidr_html)
    result = []

    full_network = []

    for cidr in cidr_list:
        if cidr not in result:
            result.append(cidr)
    
    for cidr_final,org_name in zip(result,org_list):
        print(cidr_final,org_name)
        if args.parse_cidr:
            network = cidr_parse.Parse.parse_cidr(cidr_final, do_print=can_log_network())
            data = ''
            for i in network:
                data = data + str(i) + '\n'
                full_network.append(i)
            
            output(name, data)
        else:
            output(name,cidr_final)

    if not can_log_network():
        process_module(full_network)


def can_log_network():
    return not args.test_git and not (args.test_web is not None)


isProcessingModule = False
def process_module(network_range):
    network = []
    for i in network_range:
        network.append(str(i))

    if args.test_git:
        plogger.PepperLogger.log_info('Initializing Git Exposed Scan in CIDRs.')
        #git_scanner.GitScanner.Wrapper.scan(network)

        def callback_scan(ip, port):
            git_scanner.GitScanner.Wrapper.scan([ip])

        port_scan.Scanner.Wrapper.scan_ips_with_custom_callback(network, 80, callback_scan)
        pass

    if args.test_web is not None:
        plogger.PepperLogger.log_info('Initializing Web Server Scan in CIDRs.')
        port_scan.Scanner.Wrapper.scan_ips(network, args.test_web)
        pass


def output(name,cidr_final):
    if name is not None:
        file_manager.FileManager.write(name, cidr_final, end='\n')


def msg():
    banner = '''

    )                      (                  (   (    
 ( /(  (    (     `  )    ))\ `  )   `  )    ))\  )(   
 )(_)) )\   )\ )  /(/(   /((_)/(/(   /(/(   /((_)(()\  
((_)_ ((_) _(_/( ((_)_\ (_)) ((_)_\ ((_)_\ (_))   ((_) 
/ _` |(_-<| ' \))| '_ \)/ -_)| '_ \)| '_ \)/ -_) | '_| 
\__,_|/__/|_||_| | .__/ \___|| .__/ | .__/ \___| |_|   
                 |_|         |_|    |_|         v.1.0
'''
    return banner

args = None

def init():
    global args
    parser = argparse.ArgumentParser(description=msg(), formatter_class=RawTextHelpFormatter, usage="python asnpepper.py -o org --output output.txt")
    parser.add_argument('-o','--org', dest='org', action='store', type=str, help='insert an organization', required=True)
    parser.add_argument('--output', dest='output_file', action='store', type=str, help="file to save CIDR's")
    parser.add_argument('-p', '--parse-cidr', dest='parse_cidr', help='convert cidrs to network IPs range', default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--test-git', dest='test_git', help='test IPs containing git exposed (in development)', default=False, action=argparse.BooleanOptionalAction)
    parser.add_argument('--test-port', dest='test_web', action='store', type=int, help="test IPs containing port (in development)")

    args=parser.parse_args()

    if args.test_web or args.test_git:
        args.parse_cidr = True

    main(args.org,args.output_file)



init()

#def callback_scan(ip, port):
#    git_scanner.GitScanner.Wrapper.scan([ip])

#port_scan.Scanner.Wrapper.scan_ips_with_custom_callback(['10.11.26.112'], 80, callback_scan)