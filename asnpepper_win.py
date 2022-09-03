from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from argparse import RawTextHelpFormatter
from time import sleep
import re, argparse, cidr_parse


# Test commmit
def main(org,name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
    res = browser.get("https://bgp.he.net/search?search%5Bsearch%5D="+org+"&commit=Search")
    sleep(1)
    cidr_html = browser.page_source
    cidr_html = cidr_html.replace("\t","")
    cidr_html = cidr_html.replace("\n","")
    cidr_list = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}', cidr_html)
    org_list = re.findall("(?<=0\/[0-9][0-9]<\/a><\/td><td>)([a-zA-Z,. ]{1,20})(?=<div)", cidr_html)
    result = []
    for cidr in cidr_list:
        if cidr not in result:
            result.append(cidr)
    
    for cidr_final,org_name in zip(result,org_list):
        print(cidr_final,org_name)
        if name:
            output(name,cidr_final)

def output(name,cidr_final):
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

parser = argparse.ArgumentParser(description=msg(), formatter_class=RawTextHelpFormatter, usage="python asnpepper.py -o org --output output.txt")
parser.add_argument('-o','--org', dest='org', action='store', type=str, help='insert an organization', required=True)
parser.add_argument('--output', dest='output_file', action='store', type=str, help="file to save CIDR's")
args=parser.parse_args()
main(args.org,args.output_file)

