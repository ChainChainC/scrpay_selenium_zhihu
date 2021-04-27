from scrapy import signals
from scrapy.http import HtmlResponse
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "normal"


class ZhihuSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuDownloaderMiddleware:
    def __init__(self):
        self.user_agent = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
            "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
            "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
            "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
            "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
            "Mozilla/2.02E (Win95; U)",
            "Mozilla/3.01Gold (Win95; I)",
            "Mozilla/4.8 [en] (Windows NT 5.1; U)",
            "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
            "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
            "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
        ]
        self.proxy_list = [
            'http://223.242.223.132:4225', 'http://114.106.171.186:4242', 'http://117.69.185.190:4286',
            'http://171.112.89.237:4278', 'http://121.226.212.214:4264',
            'http://59.60.140.150:4242'
        ]
        self.cookie_list = [
            [{'domain': '.zhihu.com', 'expiry': 1606392293, 'httpOnly': False, 'name': 'tst', 'path': '/', 'secure': False, 'value': 'r'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'n_c', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.zhihu.com', 'expiry': 1619352290, 'httpOnly': True, 'name': 'z_c0', 'path': '/', 'secure': False, 'value': 'Mi4xUTNVX0F3QUFBQUFBb0pmc01KQWFFaGNBQUFCaEFsVk40VnFGWUFEQklaN3RjTEZuU01IM3g3RU5XLXlUdWpCLTdn|1603800289|d29c9240eacfac969a547f1e15f52ac39be5f922'}, {'domain': '.zhihu.com', 'expiry': 1606392282, 'httpOnly': False, 'name': 'l_cap_id', 'path': '/', 'secure': False, 'value': '"MjdkMTgwZWFlZGY0NGI3MzlkNjE2NjQxYjM0MTI2NjM=|1603800282|60636b62a540a70735abc716184d97ef8d459323"'}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'osd', 'path': '/', 'secure': False, 'value': 'UVkTAElHZwlgHR5IJUe0kk4rjlEyPBZWOHYueUIwL21QcXYPZ5FplT8eG0ohhhW-LfHRVGo32jrj0YkCDRJmRKg='}, {'domain': '.zhihu.com', 'expiry': 1606392282, 'httpOnly': False, 'name': 'cap_id', 'path': '/', 'secure': False, 'value': '"Y2FiZmVjNzVjYzgzNGUwNDk3ZDkyY2Y0ZWQ3MDMzOWE=|1603800282|813b2c14c6330ad180302667719091ae25980a4b"'}, {'domain': '.zhihu.com', 'expiry': 1698408274, 'httpOnly': False, 'name': 'd_c0', 'path': '/', 'secure': False, 'value': '"AKCX7DCQGhKPTgGQn0SJUmFygyEQcYQXYIA=|1603800274"'}, {'domain': '.zhihu.com', 'expiry': 1635336293, 'httpOnly': False, 'name': 'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'secure': False, 'value': '1603800274'}, {'domain': '.zhihu.com', 'expiry': 1606392282, 'httpOnly': False, 'name': 'r_cap_id', 'path': '/', 'secure': False, 'value': '"ZmZjZTQ4NTg0MThiNDExZmEwNGRmYzQ4ODA0ZTk5ZmQ=|1603800282|ea7429e4be3647ec41dfa26839e07191cea95797"'}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'KLBRSID', 'path': '/', 'secure': False, 'value': '975d56862ba86eb589d21e89c8d1e74e|1603800300|1603800271'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49', 'path': '/', 'secure': False, 'value': '1603800294'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': 'l_n_c', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'JOID', 'path': '/', 'secure': False, 'value': 'VFEcBEtCbwZkHxtAKkO2l0YkilM3NBlSOnMmdkYyKmVfdXQKb55tlzoWFE4jgx2xKfPUXGUz2D_r3o0ACBppQKo='}, {'domain': 'www.zhihu.com', 'httpOnly': False, 'name': 'SESSIONID', 'path': '/', 'secure': False, 'value': 'yvZYj26bvJc5miEETESCpa3ChgMiUK13uzAPeWG4cDH'}, {'domain': '.zhihu.com', 'expiry': 1666872271, 'httpOnly': False, 'name': '_zap', 'path': '/', 'secure': False, 'value': '5873548e-65ef-484a-b5ce-05c21abcfd84'}, {'domain': '.zhihu.com', 'httpOnly': False, 'name': '_xsrf', 'path': '/', 'secure': False, 'value': 'e19b01af-25d4-4979-a438-a2ec1b87e4a1'}, {'domain': '.zhihu.com', 'expiry': 1606392274, 'httpOnly': True, 'name': 'capsion_ticket', 'path': '/', 'secure': False, 'value': '"2|1:0|10:1603800274|14:capsion_ticket|44:MjkyNTA2MmViOTkzNGYxMzlkMzhjN2I1ZmI1OTRjNDI=|254f3fd28fbe881cefa09c6b03e9d01304a07583646decc0045bf269b4850e6a"'}]
                            ]


    #配置driver的代理等，并实现初始化
    def driver_init(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # ip = random.choice(self.proxy_list)
        # chrome_options.add_argument('--proxy-server='+ip)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)
        # request.meta['proxy'] = random.choice(self.proxy_list)
        # print('代理IP为：', request.meta['proxy'])
        return None

    #继承spider类
    def process_response(self, request, response, spider):
        if 'zhihu' in request.url:
            driver = self.driver_init()
            driver.get(url=request.url)
            cookies = random.choice(self.cookie_list)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            js = "window.scrollTo(0,document.body.scrollHeight)"
            driver.execute_script(js)
            row_response = driver.page_source
            driver.quit()
            return HtmlResponse(url=request.url, body=row_response, encoding="utf8", request=request)
        else:
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
