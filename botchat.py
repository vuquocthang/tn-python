import helper
import json
import requests
import threading

#url = "http://192.168.81.139:8001"

url = "http://toolnuoi99.tk"

NUM_WORKERS = 1

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        clone = requests.get("{}/api/clone".format(url)).json()

        print(clone)

        driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

        try:

            helper.newest_message(driver)
            #helper.request_message(driver)

            #active_user_links = helper.active_conversations(driver)
            #helper.message_to_active_users(driver, active_user_links)
        except Exception as e:
            print(e)
        #driver.quit()

create_workers()

'''
count = 0

while(True):
    count += 1
    clone = requests.get("{}/api/clone".format(url)).json()

    print(clone)

    driver = helper._init( clone['ip'], clone['port'], clone['c_user'], clone['xs'])

    try:

        helper.newest_message(driver)
        helper.request_message(driver)

        active_user_links = helper.active_conversations(driver)
        helper.message_to_active_users(driver, active_user_links)
    except Exception as e:
        print(e)
    driver.quit()
'''