from selenium import webdriver

class Getter():
    @staticmethod
    def get_bgp(org):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        try:
            browser = webdriver.Chrome(options=options)
        except:
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        browser.get("https://bgp.he.net/search?search%5Bsearch%5D="+org+"&commit=Search") 
        cidr_html = browser.page_source
        while 'Please wait while we validate your browser.' in cidr_html:
            cidr_html = browser.page_source
        cidr_html = cidr_html.replace("\t","")
        cidr_html = cidr_html.replace("\n","")
        return cidr_html