import helper
import requests
import threading
import time
from xvfbwrapper import Xvfb
from pyvirtualdisplay import Display
import myutil.init
import myutil.log as mylog
import vip_user_helper as viphelper

url = "http://toolnuoi999.tk"

NUM_WORKERS = 1

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        try:
            clone = requests.get("{}/api/clones/Vip/comment".format(url), {
                'api_key': helper.get_api_key()
            }).json()[0]

            if clone is None:
                break

            mylog.save("comment", "{}".format(clone))

            vdisplay = Xvfb()
            vdisplay.start()
            display = Display(visible=0, size=(800, 600))
            display.start()

            driver = None

            try:
                driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                print(clone['ip'])
                print(clone['port'])

                check = myutil.init._is_checkpoint(driver, clone)

                if check is False:
                    print("Clone is checkpoint")
                    driver.quit()
                    #break
                viphelper.rep_comment_on_mobile(driver, clone['c_user'], clone['user']['vip_keywords'])

            except Exception as e:
                print("Exception : {}".format(e))
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

