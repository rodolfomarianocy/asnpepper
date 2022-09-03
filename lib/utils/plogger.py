class PepperLogger:
    @staticmethod
    def log_info(txt):
        print('[•] ' + txt)

    @staticmethod
    def log_error(txt):
        print('[-] ' + txt)

    @staticmethod
    def log_warning(txt):
        print('[!] ' + txt)

    @staticmethod
    def log_success(txt):
        print('[+] ' + txt)