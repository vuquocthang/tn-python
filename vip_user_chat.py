import os
import threading
import time

import requests

import helper
# from xvfbwrapper import Xvfb
# from pyvirtualdisplay import Display
import myutil.init
import myutil.log as mylog
import vip_user_helper as viphelper

#url = "http://toolnuoi999.tk"
url = "http://192.168.81.139:8001"

logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-chat-logging')

NUM_WORKERS = 1

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        try:
            clone = requests.get("{}/api/clones/Vip/all".format(url), {
                'api_key': helper.get_api_key()
            }).json()

            if clone is None:
                break

            mylog.save("chat", "{}".format(clone))

            #vdisplay = Xvfb()
            #vdisplay.start()
            #display = Display(visible=0, size=(800, 600))
            #display.start()

            driver = None

            try:
                driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

                check = myutil.init._is_checkpoint(driver, clone)

                if check is False:
                    print("Clone is checkpoint")
                    driver.quit()
                    #break


                viphelper.newest_message(driver, clone['user']['vip_keywords'])
                viphelper.request_message(driver, clone['user']['vip_keywords'])

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

            #display.stop()
            #vdisplay.stop()

        except Exception as e:
            print(e)

        time.sleep(5)
create_workers()

