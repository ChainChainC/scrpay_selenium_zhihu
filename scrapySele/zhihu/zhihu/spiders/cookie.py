# from selenium import webdriver
# import time
# desired_capabilities = DesiredCapabilities.CHROME
# desired_capabilities["pageLoadStrategy"] = "normal"
#
#
# def cookie_get(url):
#         cookie_list = []
#         while 1:
#             choice = input('是否获取cookie(y/n)')
#             if choice == 'y':
#                 driver = webdriver.Chrome()
#                 driver.get(url)
#                 time.sleep(30)
#                 cookies = driver.get_cookies()
#                 print(cookies)
#                 cookie_list.append(cookies)
#                 driver = webdriver.Chrome()
#                 driver.get(url)
#                 for cook in cookies:
#                     driver.add_cookie(cook)
#                 driver.refresh()
#                 driver.close()
#             else:
#                 break
#         print("自动登陆完成，获取成功")
#         return cookie_list
#
#
# if __name__ == '__main__':
#     cookie_list = cookie_get('https://www.zhihu.com/signin?next=%2F')
#     print(cookie_list)
