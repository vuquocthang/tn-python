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


# url = "http://192.168.81.139:8001"
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



def _init_with_extension(ip, port):
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
    # fp.set_preference('permissions.default.image', 2)
    # fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    # fp.set_preference("general.useragent.override", random.choice(useragents))

    extension_path = "foxyproxy@eric.h.jung.xpi"
    fp.add_extension(extension_path)

    fp.update_preferences()

    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    '''
    username = "hohzaipa"
    password = "Em4q6QYK"

    driver.execute_script("window.scrollTo(0, 1000)")

    driver.find_element_by_class_name("button").click()
    driver.find_element_by_xpath("//*[@id='mode']//option[2]").click()

    driver.find_elements_by_class_name("show-for-medium")[0].click()
    driver.find_element_by_xpath("//*[@id='newProxyType']/option[@value=3]").click()

    driver.find_element_by_id("newProxyAddress").send_keys(ip)
    driver.find_element_by_id("newProxyPort").send_keys(port)
    driver.find_element_by_id("newProxyUsername").send_keys(username)
    driver.find_element_by_id("newProxyPassword").send_keys(password)

    driver.find_element_by_id("newProxySave").click()
    '''

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

    return driver


def _init2(ip, port):
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

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference('network.proxy.http', ip)
    fp.set_preference('network.proxy.http_port', port)

    fp.set_preference('network.proxy.ssl', ip)
    fp.set_preference('network.proxy.ssl_port', port)

    fp.update_preferences()

    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    return driver


def _init(ip, port, c_user, xs):
    '''
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    firefox_capabilities['marionette'] = True
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
    fp.set_preference('permissions.default.image', 2)
    fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    fp.set_preference("general.useragent.override", random.choice(useragents))

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference('network.proxy.http', ip)
    fp.set_preference('network.proxy.http_port', port)

    fp.set_preference('network.proxy.ssl', ip)
    fp.set_preference('network.proxy.ssl_port', port)

    fp.update_preferences()

    options = Options()
    #options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)
    '''

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

    driver.get("https://www.facebook.com")
    driver.add_cookie(c_user)
    driver.add_cookie(xs)
    driver.get("https://www.facebook.com")

    driver.get("https://m.facebook.com")
    driver.add_cookie(c_user)
    driver.add_cookie(xs)
    driver.get("https://m.facebook.com")

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


def message(driver, recipient_id, message):
    try:

        driver.get("https://m.facebook.com/messages/thread/{}".format(recipient_id))

        driver.find_element_by_name('body').send_keys(message)
        driver.find_element_by_name('send').click()
    except Exception as e:
        return "error : {}".format(e)
    else:
        return True


def accept_friend(driver):
    driver.get("https://www.facebook.com")
    driver.get("https://www.facebook.com/find-friends/browser/")
    time.sleep(10)

    while True:
        items = driver.find_elements_by_class_name("friendRequestItem")

        if len(items) < 10:
            break

        for item in items:
            try:
                item.find_elements_by_tag_name('button')[0].click()
                time.sleep(1)
            except Exception as e:
                driver.execute_script("window.scrollTo(0, 50)")

        try:
            driver.find_element_by_id("FriendRequestMorePager").click()
        except Exception as e:
            driver.get("https://www.facebook.com/friends/requests/?fcref=jwl")
            print(e)


def send_message(driver, link, message):
    driver.get(link)
    driver.find_element_by_name('body').send_keys(message)
    driver.find_element_by_name('send').click()


def newest_message(driver):
    try:
        driver.get("https://m.facebook.com/messages/?folder=unread")

        conversations = driver.find_elements_by_xpath("//div[@id='root']//tbody//a[contains(@href,'/messages/read')]")

        if (len(conversations) == 0):
            return 0

        links = []

        for conversation in conversations:
            link = conversation.get_attribute('href')
            links.append(link)

        for link in links:
            try:
                print(link)
                driver.get(link)
                recipient_message = driver.find_element_by_xpath("//div[@id='fua']//span[1]").text
                recipient_name = driver.find_element_by_xpath("//div[@id='fua']//strong[1]").text

                message = get_message_from_keyword('message', recipient_message, recipient_name)

                #print(message)

                if message is not False:
                    print(message)
                    send_message(driver, link, message)
                else:
                    print("Message not has keyword")
            except Exception as e:
                print(e)
    except Exception as e:
        return "error : {}".format(e)
    else:
        return True


def get_message_from_keyword(type, message, name):
    keywords_from_server = requests.post('{}/api/keywords'.format(url), {
        'type': type
    }).json()

    for k in keywords_from_server:
        #print(k['key'].lower())
        #print(message.lower())
        if k['key'].lower() in message.lower():
            return k['value'].replace("[name]", name)

    return False


def get_random_schedule_message_from_server(type, name):
    messages_from_server = requests.post('{}/api/keywords'.format(url), {
        'type': type
    }).json()

    message = random.choice(messages_from_server)

    return message['value'].replace("[name]", name)


def request_message(driver):
    try:
        driver.get("https://m.facebook.com/messages/?folder=pending")

        conversations = driver.find_elements_by_xpath("//div[@id='root']//tbody//a[contains(@href,'/messages/read')]")

        if (len(conversations) == 0):
            return 0

        links = []

        for conversation in conversations:
            link = conversation.get_attribute('href')

            links.append(link)

        for link in links:
            try:
                print(link)
                driver.get(link)
                # send_message(driver, link, "This is a virus" )

                recipient_message = driver.find_element_by_xpath("//div[@id='fua']//span[1]").text
                recipient_name = driver.find_element_by_xpath("//div[@id='fua']//strong[1]").text

                message = get_message_from_keyword('message', recipient_message, recipient_name)

                #print(message)

                if message is not False:
                    send_message(driver, link, message)
                else:
                    print("Message not has keyword")
            except Exception as e:
                print(e)

    except Exception as e:
        return "error : {}".format(e)
    else:
        return True


def message_to_active_users(driver, links):
    for link in links:
        print(link)

        driver.get(link)

        try:
            user_name = driver.find_element_by_xpath("//div[@id='root']//span[1]").text
            message = get_random_schedule_message_from_server('schedule_message', user_name)

            send_message(driver, link, message)
        except Exception as e:
            user_name = driver.find_element_by_xpath("//form[@id='composer_form']//li[1]").text
            message = get_random_schedule_message_from_server('schedule_message', user_name)
            driver.find_element_by_name('body').send_keys(message)
            driver.find_element_by_name('Send').click()


def add_friend(driver, uid):
    driver.get("https://m.facebook.com/{}".format(uid))
    try:
        driver.find_element_by_xpath("//a[contains(text(), 'Add Friend')]").click()
        driver.find_element_by_xpath("//a[contains(text(), 'OK')]").click()
    except Exception as e:
        driver.find_element_by_xpath("//a[contains(text(), 'Thêm bạn bè')]").click()


def active_conversations(driver):
    try:
        driver.get("https://m.facebook.com/buddylist.php")

        conversations = driver.find_elements_by_xpath("//div[@id='root']//tbody//a[contains(@href,'/messages/read')]")

        if (len(conversations) == 0):
            return 0

        links = []

        for conversation in conversations:
            link = conversation.get_attribute('href')

            links.append(link)

    except Exception as e:
        print("error : {}".format(e))
        return False
    else:
        return links


def up_avatar(driver, image_path):
    driver.get('https://m.facebook.com/profile_picture')
    driver.find_element_by_name('pic').send_keys(image_path)
    driver.find_element_by_xpath("//input[@type='button']").click()
    driver.find_element_by_xpath("//input[@type='submit']").click()


def happy_birthday(driver, message):
    driver.get("https://m.facebook.com/events/birthdays")

    a_elements = driver.find_elements_by_xpath("//td[@id='events_card_list']/div[1]//a")

    links_to_happybirthday = []

    for a in a_elements:
        link = a.get_attribute('href')
        print(link)
        links_to_happybirthday.append(link)

    # print(links_to_happybirthday)
    links_to_happybirthday = set(links_to_happybirthday)
    print(links_to_happybirthday)

    for link in links_to_happybirthday:
        driver.get(link)
        driver.find_element_by_name("xc_message").send_keys(message)
        driver.find_element_by_name("view_post").click()
        time.sleep(15)

    '''
    inputs = driver.find_elements_by_name('message')
    post_buttons = driver.find_elements_by_xpath("//input[@value='Post']")

    if( len(post_buttons) == 0 ):
        post_buttons = driver.find_elements_by_xpath("//input[@value='Đăng']")

    for index, input in enumerate(inputs):
        input.send_keys(message)
        post_buttons[index].click()
        driver.get("https://m.facebook.com/events/birthdays")

        time.sleep(5)
    '''

def happy_birthday2(driver):
    driver.get("https://m.facebook.com/events/birthdays")
    events_card_list = driver.find_elements_by_xpath("//*[@id='events_card_list']//ul[1]/div")

    links_and_names = []

    for item in events_card_list:
        try:
            #links.append(item.find_elements_by_tag_name("a")[0].get_attribute("href") )
            name = item.find_elements_by_tag_name("a")[0].find_elements_by_tag_name("div")[0].find_elements_by_tag_name("div")[0].text

            tmp = {
                'link' : item.find_elements_by_tag_name("a")[0].get_attribute("href"),
                'name' : name
            }

            links_and_names.append(tmp)

        except Exception as e:
            print(e)


    print(links_and_names)

    for item in links_and_names:
        print(item)
        try:
            driver.get(item['link'])

            message = get_random_schedule_message_from_server('birthday', item['name'])

            driver.find_element_by_name("xc_message").send_keys(message)
            driver.find_element_by_name("view_post").click()
        except Exception as e:
            print("Post ex : {}".format(e))



def get_friends(driver):
    driver.get("")


def get_friend_list(token):
    r = requests.get("https://graph.facebook.com/me/friends?limit=5000", {
        'access_token': token
    }).json()

    return r['data']


def like_first_post(driver, uid):
    driver.get("https://m.facebook.com/{}?v=timeline".format(uid))

    try:
        driver \
            .find_element_by_xpath(
            "//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'Thích')][1]") \
            .click()
    except Exception as e:
        driver \
            .find_element_by_xpath(
            "//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'Like')][1]") \
            .click()


def react_first_post(driver, uid, type):
    driver.get("https://m.facebook.com/{}?v=timeline".format(uid))
    driver \
        .find_element_by_xpath(
        "//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'React')][1]") \
        .click()

    driver \
        .find_element_by_xpath("//span[contains(text(), '{}')][1]".format(type)) \
        .click()


def post_status(driver, text, image_paths):

    print("Image paths : {}".format(image_paths))

    if len(image_paths) > 0:
        paths = image_paths[:3]
        # click to where upload image
        print("click to where upload image")

        try:
            wait = WebDriverWait(driver, 15)
            view_photo = wait.until(EC.presence_of_element_located((By.NAME, 'view_photo')))
            view_photo.click()
        except Exception as e:
            print("click view_photo ex : {}".format(e))

        print("click to where upload image done")

        time.sleep(3)

        driver.save_screenshot('post-click-view-photo.png')

        driver.implicitly_wait(10)
        print("begin upload images")

        # upload image
        for index, path in enumerate(paths):

            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.NAME, 'file{}'.format(index + 1)))
                )

                element.send_keys(path)
            except Exception as e:
                driver.find_element_by_name('file{}'.format(index + 1)).send_keys(path)
                driver.save_screenshot('post-upload-file.png')

        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "add_photo_done"))
            )

            element.click()
        except Exception as e:
            #driver.find_element_by_name('add_photo_done').click()
            print("Click add photo done ex : {}".format(e))

        time.sleep(20)
        driver.find_element_by_name('xc_message').send_keys(text)

        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
            element.click()

        except Exception as e:
            time.sleep(20)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
            element.click()
    else:
        driver.find_element_by_name('xc_message').send_keys(text)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
        element.click()


def post_status2(driver, text, image_paths):
    time.sleep(5)

    for path in image_paths:
        print(path)
        driver.find_element_by_name("composer_photo[]").send_keys(path)

    driver.find_element_by_class_name("navigationFocus").send_keys(text)
    driver.save_screenshot("navigationFocus.png")

    time.sleep(15)
    driver.find_elements_by_class_name("selected")[1].click()
    driver.save_screenshot("post.png")

def react_post_in_newfeeds(driver, type):
    #type : 1 - 6 { "like", "love", "haha", "wow", "sad", "angry" }

    driver.get("https://m.facebook.com")

    driver.find_element_by_xpath("//div[@id='m_newsfeed_stream']//div[@role='article'][1]")\
        .find_element_by_xpath("//a[contains(@href, 'reactions/picker')][1]")\
        .click()

    driver.find_element_by_xpath("//div[@id='root']//li[{}]".format(type))\
        .click()
    time.sleep(2)

    driver.save_screenshot("react-done.png")


def rep_comment(driver, uid):
    # go to profile
    driver.get("https://www.facebook.com/{}".format(uid))
    time.sleep(3)

    # scroll down
    # for i in range(5):
    driver.execute_script("window.scrollTo(0, 50000)")

    # sleep 3 s
    # time.sleep(5)

    # remove comments that were replied
    '''
    var UFIRows = document.getElementsByClassName("UFIRow");

    for(i=0; i< UFIRows.length; i++){
        if( UFIRows[i].nextElementSibling != null ){
            if(UFIRows[i].nextElementSibling.className.includes("UFIReplyList") ){
                UFIRows[i].nextElementSibling.remove();
                UFIRows[i].remove();
            }
        }
    }
    '''
    script_to_remove_comments = 'var UFIRows = document.getElementsByClassName("UFIComment");'
    script_to_remove_comments += 'for(i=0; i< UFIRows.length; i++){'
    script_to_remove_comments += '  if( UFIRows[i].nextElementSibling != null ){'
    script_to_remove_comments += '      if(UFIRows[i].nextElementSibling.className.includes("UFIReplyList") ){'
    script_to_remove_comments += '          UFIRows[i].nextElementSibling.remove();'
    script_to_remove_comments += '          UFIRows[i].remove();'
    script_to_remove_comments += '      }'
    script_to_remove_comments += '  }'
    script_to_remove_comments += '}'

    print(script_to_remove_comments)
    driver.execute_script(script_to_remove_comments)
    driver.execute_script(script_to_remove_comments)

    # scroll down
    # driver.execute_script("window.scrollTo(0, 5000)")

    time.sleep(10)

    # get post items
    post_items = driver.find_elements_by_xpath("//div[contains(@id, 'tl_unit_')]")

    for item in post_items:
        try:
            newest_cmts = item.find_elements_by_class_name("UFIRow")
            reply_buttons = item.find_elements_by_class_name("UFICommentActions")

            for index in range(len(newest_cmts)):
                print("cmt : {}".format(newest_cmts[index].find_element_by_class_name("UFICommentActorAndBody").text))
                # UFIReplyLink
                reply_buttons[index].find_element_by_class_name("UFIReplyLink").click()

                time.sleep(1)

                # input
                inputs = item.find_elements_by_class_name("notranslate")
                inputs[index].send_keys("Cmt")
                inputs[index].send_keys(Keys.ENTER)

                time.sleep(3)
        except Exception as e:
            print(e)


            # return len(post_items[:10])


def rep_comment_on_mobile(driver, uid):
    driver.get("https://m.facebook.com/{}".format(uid))
    articles = driver.find_elements_by_xpath("//div[@id='structured_composer_async_container']//div//div")

    comment_links = []

    for article in articles[:10]:
        link = article.find_element_by_xpath("//a[contains(@href, 'story.php')]")
        comment_links.append(link.get_attribute("href"))

    print(comment_links)


    driver.get(comment_links[0])
    comment_items = driver.find_elements_by_xpath("//div[@id='m_story_permalink_view']/div[2]/div[1]/div[4]/div")

    comments_and_rep_links = []

    for item in comment_items:
        #print(item.text)
        #print(item.get_attribute('id'))

        comment = driver.find_element_by_xpath("//div/div[1]").text
        print(comment)

        rep_link = item.find_element_by_xpath("//a[contains(@href, '/comment/reply')][1]").get_attribute("href")

        print(rep_link)

        comments_and_rep_links.append({
            'comment' : comment,
            'rep_link' : rep_link
        })



    for item in comments_and_rep_links:
        driver.get(item['rep_link'])
        driver.find_element_by_id("composerInput").send_keys("Thanks")
        driver.find_element_by_xpath("//*[@type='submit']").click()
