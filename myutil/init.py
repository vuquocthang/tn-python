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
from selenium.webdriver.common.keys import Keys
import json
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.firefox_profile import AddonFormatError

class FirefoxProfileWithWebExtensionSupport(webdriver.FirefoxProfile):
    def _addon_details(self, addon_path):
        try:
            return super()._addon_details(addon_path)
        except AddonFormatError:
            try:
                with open(os.path.join(addon_path, 'manifest.json'), 'r') as f:
                    manifest = json.load(f)
                    return {
                        'id': manifest['applications']['gecko']['id'],
                        'version': manifest['version'],
                        'name': manifest['name'],
                        'unpack': False,
                    }
            except (IOError, KeyError) as e:
                raise AddonFormatError(str(e), sys.exc_info()[2])

url = "http://toolnuoi999.tk"

useragents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996",
    "Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10",
    "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4",
    "Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30"
]

def _init_with_useragent(ip, port, c_user, xs, useragent):
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['acceptInsecureCerts'] = True
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/local/bin/geckodriver'
    firefox_capabilities['acceptUntrustedCertificates'] = True
    firefox_capabilities['assumeUntrustedCertificateIssuer'] = True
    firefox_capabilities['acceptNextAlert'] = True

    fp = FirefoxProfileWithWebExtensionSupport()
    fp.accept_untrusted_certs = True
    fp.assume_untrusted_cert_issuer = True
    fp.accept_next_alert = True
    fp.set_preference('permissions.default.image', 2)
    fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    fp.set_preference("general.useragent.override", useragent)

    extension_path = "foxyproxy@eric.h.jung.xpi"
    fp.add_extension(extension_path)
    fp.update_preferences()

    options = Options()
    #options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    try:
        username = "hohzaipa"
        password = "Em4q6QYK"
        driver.execute_script("window.scrollTo(0, 2000)")
        driver.save_screenshot("login-proxy.png")

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "button"))
            )

            element.click()
        except Exception as e:
            print(e)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mode']//option[2]"))
            )

            element.click()
        except Exception as e:
            print(e)

            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='mode']//option[2]"))
            )

            element.click()

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@class='show-for-medium'][1]"))
            )

            element.click()
        except Exception as e:
            print(e)


        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='newProxyType']/option[@value=3]"))
            )

            element.click()
        except Exception as e:
            print(e)

            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='newProxyType']/option[@value=3]"))
            )

            element.click()


        driver.find_element_by_id("newProxyAddress").send_keys(ip)
        driver.find_element_by_id("newProxyPort").send_keys(port)
        driver.find_element_by_id("newProxyUsername").send_keys(username)
        driver.find_element_by_id("newProxyPassword").send_keys(password)
        driver.find_element_by_id("newProxySave").click()
    except Exception as e:
        print("Login proxy exception : {}".format(e))

    driver.get("https://facebook.com")
    c_user = {
        "domain": ".facebook.com",
        'name': 'c_user',
        'value': c_user
    }
    xs = {
        "domain": ".facebook.com",
        "name": "xs",
        "value": xs
    }
    driver.add_cookie(c_user)
    driver.add_cookie(xs)
    #driver.get("https://m.facebook.com")
    return driver


def _init_with_extension_not_use(ip, port):
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/local/bin/geckodriver'
    firefox_capabilities['acceptInsecureCerts'] = True
    firefox_capabilities['acceptUntrustedCertificates'] = True
    firefox_capabilities['assumeUntrustedCertificateIssuer'] = True
    firefox_capabilities['acceptNextAlert'] = True

    # fp = webdriver.FirefoxProfile()
    fp = FirefoxProfileWithWebExtensionSupport()

    fp.accept_untrusted_certs = True
    fp.assume_untrusted_cert_issuer = True
    # fp.setAcceptUntrustedCertificates = True
    # fp.setAssumeUntrustedCertificateIssuer = False
    fp.accept_next_alert = True
    fp.set_preference('permissions.default.image', 2)
    fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # fp.set_preference("general.useragent.override", random.choice(useragents))

    extension_path = "foxyproxy@eric.h.jung.xpi"
    fp.add_extension(extension_path)

    fp.update_preferences()

    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    return  driver

def _init_with_extension(ip, port):
    print("init with extension")

    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['marionette'] = True
    firefox_capabilities['binary'] = '/usr/local/bin/geckodriver'
    firefox_capabilities['acceptInsecureCerts'] = True
    firefox_capabilities['acceptUntrustedCertificates'] = True
    firefox_capabilities['assumeUntrustedCertificateIssuer'] = True
    firefox_capabilities['acceptNextAlert'] = True

    # fp = webdriver.FirefoxProfile()
    fp = FirefoxProfileWithWebExtensionSupport()

    fp.accept_untrusted_certs = True
    fp.assume_untrusted_cert_issuer = True
    # fp.setAcceptUntrustedCertificates = True
    # fp.setAssumeUntrustedCertificateIssuer = False
    fp.accept_next_alert = True
    fp.set_preference('permissions.default.image', 2)
    fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # fp.set_preference("general.useragent.override", random.choice(useragents))

    extension_path = "foxyproxy@eric.h.jung.xpi"
    fp.add_extension(extension_path)

    fp.update_preferences()

    options = Options()
    #options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    username = "hohzaipa"
    password = "Em4q6QYK"


    count = 0

    while "moz-extension" not in driver.current_url:
        print(driver.current_url)
        count = count + 1

        #if count == 20:
            #break
        time.sleep(3)

        if count == 5:
            driver.quit()
            driver = _init_with_extension_not_use(ip, port)

    print(driver.current_url)

    current_url = driver.current_url
    new_url = current_url.replace("first-install.html", "proxies.html")

    print(new_url)

    driver.get(new_url)

    '''
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Ok')][1]"))
        )

        element.click()
    except Exception as e:
        print(e)
        driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        try:
            driver.find_element_by_class_name("button").click()
        except Exception as e:
            time.sleep(3)
            driver.find_element_by_class_name("button").click()
    '''

    #driver.find_element_by_xpath("//*[@id='mode']//option[2]").click()

    time.sleep(3)
    mode = Select(driver.find_element_by_id("mode"))
    mode.select_by_index(1)

    time.sleep(3)
    driver.find_elements_by_class_name("show-for-medium")[0].click()

    #driver.find_element_by_xpath("//*[@id='newProxyType']/option[@value=3]").click()

    time.sleep(3)
    proxy_type = Select(driver.find_element_by_id("newProxyType"))
    proxy_type.select_by_index(1)

    time.sleep(3)
    driver.find_element_by_id("newProxyAddress").send_keys(ip)
    driver.find_element_by_id("newProxyPort").send_keys(port)
    driver.find_element_by_id("newProxyUsername").send_keys(username)
    driver.find_element_by_id("newProxyPassword").send_keys(password)

    driver.find_element_by_id("newProxySave").click()

    return driver

def _init(ip, port, c_user, xs):
    driver = _init_with_extension(ip, port)

    c_user = {
        "domain": ".facebook.com",
        'name': 'c_user',
        'value': c_user
    }
    xs = {
        "domain": ".facebook.com",
        "name": "xs",
        "value": xs
    }

    driver.get("https://m.facebook.com/login")
    driver.add_cookie(c_user)
    driver.add_cookie(xs)
    driver.get("https://m.facebook.com/login")

    return driver

def _init_desktop(ip, port, c_user, xs):
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
    # fp.set_preference('permissions.default.image', 2)
    # fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # fp.set_preference("general.useragent.override", random.choice(useragents))
    fp.set_preference("dom.webnotifications.enabled", False)

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference('network.proxy.http', ip)
    fp.set_preference('network.proxy.http_port', port)

    fp.set_preference('network.proxy.ssl', ip)
    fp.set_preference('network.proxy.ssl_port', port)

    fp.update_preferences()

    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    driver.get("https://www.facebook.com")

    c_user = {'name': 'c_user', 'value': c_user}
    driver.add_cookie(c_user)

    xs = {'name': 'xs', 'value': xs}
    driver.add_cookie(xs)

    time.sleep(3)

    driver.get("https://www.facebook.com")

    return driver

def _is_checkpoint(driver, clone):
    current_url = driver.current_url

    if "checkpoint" in current_url:
        #update clone status
        try:
            _update_clone_status(clone, "Checkpoint")
        except Exception as e:
            print(e)
        else:
            print("Update clone's status successfully !")

        return False

    if "login" in current_url:
        # update clone status
        try:
            _update_clone_status(clone, "Cookie Die")
        except Exception as e:
            print(e)
        else:
            print("Update clone's status successfully !")

        return False


    return  driver

def _update_clone_status(clone, status):
    requests.put("{}/api/clone/{}".format(url, clone['id']) , {
        'status' : status
    })

