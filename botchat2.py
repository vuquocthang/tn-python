import helper
import json
import requests
import threading
from pyvirtualdisplay import Display

url = "http://192.168.81.139:8001"

NUM_WORKERS = 5

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        clone = requests.get("{}/api/clone".format(url)).json()

        print(clone)

        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

        try:

            helper.newest_message(driver)
            helper.request_message(driver)

            active_user_links = helper.active_conversations(driver)
            helper.message_to_active_users(driver, active_user_links)
        except Exception as e:
            print(e)
        driver.quit()
        display.stop()

create_workers()
