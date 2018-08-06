import helper
import json
import requests
import threading
from pyvirtualdisplay import Display
import time
<<<<<<< HEAD
from xvfbwrapper import Xvfb

url = "http://toolnuoi999.tk"
=======
import sys, os
from xvfbwrapper import Xvfb
import logging

url = "http://toolnuoi999.tk"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-chat-logging')
logging.basicConfig(filename='chat.log',level=logging.DEBUG)

logging.info("Logging path : {}".format(logging_path))
>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624

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
<<<<<<< HEAD

            print(clone)
=======
            print(clone)

            logging.info("Start clone : {}".format(clone['uid']))
>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624

            vdisplay = Xvfb()
            vdisplay.start()
            display = Display(visible=0, size=(800, 600))
            display.start()

            driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

            try:
<<<<<<< HEAD

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
=======
                helper.newest_message(driver)
                helper.request_message(driver)

                #active_user_links = helper.active_conversations(driver)
                #helper.message_to_active_users(driver, active_user_links)
            except Exception as e:
                print("Ex 1 : {}".format(e))

                driver.save_screenshot(
                    os.path.join( logging_path , 'chat-exception-{}.{}'.format( clone['c_user'], 'png'))
                )
                driver.quit()
                display.stop()
                vdisplay.stop()
            else:
                driver.save_screenshot(
                    os.path.join(logging_path, 'chat-success-{}.{}'.format(clone['c_user'], 'png'))
                )

                driver.quit()
                display.stop()
                vdisplay.stop()
>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624
        except Exception as e:
            print(e)

        time.sleep(5)
create_workers()
