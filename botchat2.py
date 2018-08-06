import helper
import json
import requests
import threading
from pyvirtualdisplay import Display
import time
from xvfbwrapper import Xvfb

url = "http://toolnuoi999.tk"

NUM_WORKERS = 2

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        try:
            clone = requests.get("{}/api/clone".format(url)).json()

            print(clone)

            vdisplay = Xvfb()
            vdisplay.start()
            display = Display(visible=0, size=(800, 600))
            display.start()

            driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

            try:

                helper.newest_message(driver)
                helper.request_message(driver)

                #active_user_links = helper.active_conversations(driver)
                #helper.message_to_active_users(driver, active_user_links)
            except Exception as e:
                print("Ex 1 : {}".format(e))

            driver.save_screenshot('log-{}.{}'.format( clone['c_user'], 'png' ))
            driver.quit()
            display.stop()
            vdisplay.stop()
        except Exception as e:
            print(e)

        time.sleep(5)
create_workers()
