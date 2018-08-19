from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.firefox.options import Options
import os
import sys
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType

import helper

'''
myProxy = "51.15.227.220:3128"

firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
# firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = 'geckodriver.exe'
firefox_capabilities['acceptInsecureCerts'] = True
firefox_capabilities['acceptUntrustedCertificates'] = True
firefox_capabilities['assumeUntrustedCertificateIssuer'] = True
firefox_capabilities['acceptNextAlert'] = True

fp = webdriver.FirefoxProfile()
fp.accept_untrusted_certs = True
fp.assume_untrusted_cert_issuer = True
# fp.setAcceptUntrustedCertificates = True
# fp.setAssumeUntrustedCertificateIssuer = False
fp.accept_next_alert = True


fp.set_preference("network.proxy.type", 1)
fp.set_preference('network.proxy.http', "51.15.227.220")
fp.set_preference('network.proxy.http_port', 3128)

fp.set_preference('network.proxy.ssl', "51.15.227.220")
fp.set_preference('network.proxy.ssl_port', 3128)


fp.update_preferences()

options = Options()

driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

#driver.get('http://whatismyip.host/')


driver.get("https://m.facebook.com")

cookie_dict = { 'name' : 'c_user', 'value' : '100025055117657' }
driver.add_cookie(cookie_dict)

cookie_dict = { 'name' : 'xs', 'value' : '32%3A6UmlBxPGvbIkQg%3A2%3A1522086654%3A-1%3A-1' }
driver.add_cookie(cookie_dict)

driver.get("https://m.facebook.com")
driver.get("https://m.facebook.com/messages/thread/100011668026584")

driver.find_element_by_name('body').send_keys('abcd')
driver.find_element_by_name('send').click()
'''

ip = "176.108.47.38"
port = 3128

c_user = '100013406775660'
xs = '42%3AWIQhxb_ZUQtdWw%3A2%3A1529281492%3A2237%3A6251'
#recipient_id = '100011668026584'
message = 'Xin chào'


'''
while(True):
    driver = helper._init(ip, port)
    #helper.message(driver, c_user, xs, recipient_id, message)
    helper.newest_message(driver, c_user, xs)
    driver.quit()

    time.sleep(10)
'''


helper._init_with_useragent(ip, port)

#driver = helper._init(ip, port, c_user, xs)
#helper.up_avatar(driver, os.getcwd()+"\\avatars\\a.jpg")
#message = "Chúc mừng sinh nhật"

#helper.happy_birthday(driver, message)

#helper.message(driver, c_user, xs, recipient_id, message)
#helper.newest_message(driver, message)
#driver.quit()
#active_conversations = helper.active_conversations(driver)
#print(active_conversations)

'''
uids  = [
    '100011668026584',
    '100004086122196',
    '100008142038039',
    '100011505255124',
    '100021722421927',
    '100012323105979',
    '100005000386196',
    '100016481881153',
    '100024281617327',
    '100007324654796',
    '100003006073815',
    '100004906892695',
    '100013449164615',
    '100006946448779'
]

for uid in uids:
    try:
        helper.add_friend(driver, uid)
    except Exception as e:
        print( e )
'''