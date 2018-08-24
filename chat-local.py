import helper
import requests
import threading
import time
import os
import logging
import myutil.init

url = "http://toolnuoi999.tk"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-chat-logging')
logging.basicConfig(filename='chat.log',level=logging.DEBUG)

#logging.info("Logging path : {}".format(logging_path))

NUM_WORKERS = 1

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        try:
            clone = requests.get("{}/api/clone/Live".format(url)).json()

            if clone is None:
                break

            print(clone)
            driver = None

            try:
                driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                helper.newest_message(driver)
                helper.request_message(driver)

                #active_user_links = helper.active_conversations(driver)
                #helper.message_to_active_users(driver, active_user_links)
            except Exception as e:
                print("Exception : {}".format(e))
                driver.quit()
            finally:
                driver.quit()

        except Exception as e:
            print(e)

        time.sleep(5)
create_workers()
