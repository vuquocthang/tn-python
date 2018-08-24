import helper
import requests
import threading
import logging
import time
import os
from xvfbwrapper import Xvfb
from pyvirtualdisplay import Display
import myutil.init


url = "http://toolnuoi999.tk"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-chat-logging')
logging.basicConfig(filename='chat.log',level=logging.DEBUG)

logging.info("Logging path : {}".format(logging_path))

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

            logging.info("Start clone : {}".format(clone['uid']))

            vdisplay = Xvfb()
            vdisplay.start()
            display = Display(visible=0, size=(800, 600))
            display.start()

            driver = None

            try:
                driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

                check = myutil.init._is_checkpoint(driver, clone)

                if check is False:
                    print("Clone is checkpoint")
                    driver.quit()
                    break

                helper.newest_message(driver)
                helper.request_message(driver)

                #active_user_links = helper.active_conversations(driver)
                #helper.message_to_active_users(driver, active_user_links)

                driver.save_screenshot(
                    os.path.join(logging_path, 'chat-success-{}.{}'.format(clone['c_user'], 'png'))
                )
            except Exception as e:
                print("Exception : {}".format(e))

                driver.save_screenshot(
                    os.path.join( logging_path , 'chat-exception-{}.{}'.format( clone['c_user'], 'png'))
                )
                driver.quit()
            finally:
                driver.quit()
                print("Done")


            display.stop()
            vdisplay.stop()

        except Exception as e:
            print(e)

        time.sleep(5)
create_workers()
