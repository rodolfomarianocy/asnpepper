#!/usr/bin/python3

from argparse import RawTextHelpFormatter
from ast import arg
import re, argparse, sys

### include lib/utils ###
sys.path.insert(1, 'lib/utils')
#########################

import cidr_parse, cidr_getter


def main(org,name):
    cidr_html = cidr_getter.Getter.get_bgp(org)
    cidr_list = cidr_parse.Parse.extract_cidr_list(cidr_html)
    org_list = cidr_parse.Parse.extract_org_list(cidr_html)
    result = []
    for cidr in cidr_list:
        if cidr not in result:
            result.append(cidr)
    
    for cidr_final,org_name in zip(result,org_list):
        print(cidr_final,org_name)
        if args.parse_cidr:
            ip = cidr_parse.Parse.parse_cidr(cidr_final, do_print=True)
            output(name, str(ip))
        else:
            output(name,cidr_final)


def output(name,cidr_final):
    if name is not None:
        with open(name, "a") as file:
            file.write(cidr_final+"\n")


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
    args=parser.parse_args()
    main(args.org,args.output_file)

init()