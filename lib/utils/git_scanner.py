import requests, sys
from time import sleep
from threading import Thread
import os

sys.path.append( os.path.dirname(os.path.realpath(__file__))+'/../tests')

import faker, plogger


requests.packages.urllib3.disable_warnings()


class GitScanner:
    patterns = [
        '%s/HEAD',
        '%s/hooks',
        '%s/logs',
        '%s/logs/HEAD',
        '%s/objects',
        '%s/objects/info',
        '%s/objects/pack',
        '%s/refs',
        '%s/refs/heads',
        '%s/refs/remote',
        '%s/refs/remotes/origin/HEAD',
        '%s/refs/remotes/origin/master',
        '%s/info/exclude',
        '%s/config',
        '%s/description',
        '%s/FETCH_HEAD',
        '%s/ORIG_HEAD',
        '%s/packed-refs'
    ]

    git_founds = []

    def __init__(self) -> None:
        pass

    def git_exists_callback(self, url):
        print(url)
        

    def req_git(self, url, do_print=True):
        fp_prefix = ''
        try:
            test = requests.get(url + '/dsadsaudusadhd78d/', verify=False)
            if test.status_code != 404 or test.status_code == 200:
                plogger.PepperLogger.log_warning('Possible False Positive!')
                fp_prefix = '[FP Code %s] ' % (str(test.status_code))
                return
        except:
            pass


        for p in self.patterns:
            path = '/' + (p % ('.git'))
            full_path = url + path
            try:
                #print("Trying: " + full_path)
                res = requests.get(full_path)
                if res.status_code != 404:
                    if do_print:
                        print(fp_prefix + full_path)
                    self.git_founds.append(full_path)
            except requests.exceptions.ConnectionError as e:
                #print(e)
                pass
        return
    

    def scan(self, urls, schema='http://'):
        for url in urls:
            thread = Thread(target=self.req_git, args=(schema + url, True))
            thread.start()


    class Wrapper:
        @staticmethod
        def scan(urls, schema='http://'):
            GitScanner().scan(urls)