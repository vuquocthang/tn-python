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

#url = "http://192.168.81.139:8001"
url = "http://toolnuoi999.tk"

image_chat_logging_folder = "image-chat-logging"
image_post_logging_folder = "image-post-logging"
image_addfriend_logging_folder = "image-addfriend-logging"

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

def _init_with_useragent(ip, port):
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

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    driver.get("https://m.facebook.com")

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
    #fp.set_preference('permissions.default.image', 2)
    #fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
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
    #fp.set_preference("general.useragent.override", random.choice(useragents))

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference('network.proxy.http', ip)
    fp.set_preference('network.proxy.http_port', port)

    fp.set_preference('network.proxy.ssl', ip)
    fp.set_preference('network.proxy.ssl_port', port)

    fp.update_preferences()

    options = Options()
    #options.add_argument("--headless")

    driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)

    driver.get("https://m.facebook.com")

    c_user = {'name': 'c_user', 'value': c_user}
    driver.add_cookie(c_user)

    xs = {'name': 'xs', 'value': xs}
    driver.add_cookie(xs)

    time.sleep(3)

    driver.get("https://m.facebook.com")

    driver.get("https://upload.facebook.com")


    driver.add_cookie(c_user)


    driver.add_cookie(xs)

    time.sleep(3)

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
    fp.set_preference('permissions.default.image', 2)
    fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
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

    driver.get("https://facebook.com")

    c_user = {'name': 'c_user', 'value': c_user}
    driver.add_cookie(c_user)

    xs = {'name': 'xs', 'value': xs}
    driver.add_cookie(xs)

    time.sleep(3)

    driver.get("https://facebook.com")

    return driver

def message(driver, recipient_id , message):
    try:

        driver.get("https://m.facebook.com/messages/thread/{}".format(recipient_id) )

        driver.find_element_by_name('body').send_keys(message)
        driver.find_element_by_name('send').click()
    except Exception as e:
        return "error : {}".format(e)
    else:
        return True

def send_message(driver, link, message):
    driver.get(link)
    driver.find_element_by_name('body').send_keys( message )
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

                if message is not False:
                    send_message(driver, link, message )
            except Exception as e:
                print("Go to conversation exception : {}".format(e))
    except Exception as e:
        print("Send newest message error : {}".format(e))
        return False
    else:
        return True

def get_message_from_keyword(type, keyword, name):
    keywords_from_server = requests.post('{}/api/keywords'.format(url), {
        'type' : type
    }).json()

    for k in keywords_from_server:
        if keyword.lower() in k['key'].lower():
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

        if( len(conversations) == 0 ):
            return 0

        links = []

        for conversation in conversations:

            link = conversation.get_attribute('href')

            links.append(link)

        for link in links:
            try:
                print(link)
                driver.get(link)
                #send_message(driver, link, "This is a virus" )

                recipient_message = driver.find_element_by_xpath("//div[@id='fua']//span[1]").text
                recipient_name = driver.find_element_by_xpath("//div[@id='fua']//strong[1]").text

                message = get_message_from_keyword('message', recipient_message, recipient_name)

                #print(message)

                send_message(driver, link, message)
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

        if( len(conversations) == 0 ):
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
        print( link )
        links_to_happybirthday.append(link)

    #print(links_to_happybirthday)
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

def get_friends(driver):
    driver.get("")

def get_friend_list(token):
    r = requests.get("https://graph.facebook.com/me/friends?limit=5000", {
        'access_token' : token
    }).json()

    return r['data']

def like_first_post(driver, uid):
    driver.get("https://m.facebook.com/{}?v=timeline".format(uid) )

    try:
        driver\
            .find_element_by_xpath("//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'Thích')][1]")\
            .click()
    except Exception as e:
        driver\
            .find_element_by_xpath("//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'Like')][1]")\
            .click()

def react_first_post(driver, uid, type):
    driver.get("https://m.facebook.com/{}?v=timeline".format(uid))
    driver\
        .find_element_by_xpath("//div[@id='structured_composer_async_container']/div[1]/div[1]//a[contains(text(), 'React')][1]")\
        .click()

    driver\
        .find_element_by_xpath("//span[contains(text(), '{}')][1]".format(type))\
        .click()

def post_status(driver, text, image_paths):


    paths = image_paths[:3]

    if len(paths) > 0:
        #click to where upload image
        print("click to where upload image")

        try:
            wait = WebDriverWait(driver, 10)
            view_photo = wait.until(EC.presence_of_element_located((By.NAME, 'view_photo')))
            view_photo.click()
        except Exception as e:
            driver.find_element_by_name('view_photo').click()
            driver.save_screenshot('post-click-view-photo.png')
        print("click to where upload image done")

        time.sleep(3)

        driver.save_screenshot('post-click-view-photo.png')

        #upload image

        for index, path in enumerate(paths):

            try:
                element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.NAME, 'file{}'.format(index + 1)))
                )

                element.send_keys(path)
            except Exception as e:
                driver.find_element_by_name('file{}'.format(index + 1)).send_keys(path)
                driver.save_screenshot('post-upload-file.png')

        '''
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'file1' ))
        )
        element.send_keys(image_paths[0])
        '''

        driver.find_element_by_name('add_photo_done').click()
        time.sleep(20)
        driver.find_element_by_name('xc_message').send_keys(text)

        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
            element.click()

            #driver.find_element_by_name('view_post').click()
        except Exception as e:
            time.sleep(20)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
            element.click()
            #driver.find_element_by_name('view_post').click()
    else:
        #driver.find_element_by_name('view_post').click()
        driver.find_element_by_name('xc_message').send_keys(text)

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.NAME, 'view_post')))
        element.click()

        #driver.find_element_by_xpath('//input[@value="Post"]').click()

def post_status2(driver, text, image_paths):
    driver.get("https://m.facebook.com/#")
    driver.execute_script("console.log('foo')")
    #time.sleep(3)

    script = 'document.querySelector("[data-contents = {}]").click() ;'.format("'true'")

    print(script)

    driver.execute_script(script)

    #driver.find_element_by_xpath("//br[@data-text='true']").send_keys(text)


    #driver.find_element_by_class_name("notranslate").send_keys(text)
    #driver.find_element_by_xpath("//div[@data-testid='react-composer-post-button']").click()

