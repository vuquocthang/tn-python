import helper
import requests
import logging
import os
import myutil.init
from xvfbwrapper import Xvfb
from pyvirtualdisplay import Display

url = "http://toolnuoi999.tk"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-happy-birthday')
logging.basicConfig(filename='happybirthday.log',level=logging.DEBUG)

logging.info("Logging path : {}".format(logging_path))

live_clones = requests.get("{}/api/clones/Live".format(url)).json()

for clone in live_clones:
    vdisplay = Xvfb()
    vdisplay.start()
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = None

    try:
        ip = clone['ip']
        port = clone['port']
        c_user = clone['c_user']
        xs = clone['xs']

        driver = myutil.init._init(ip, port, c_user, xs)
        check = myutil.init._is_checkpoint(driver, clone)

        if check is False:
            driver.quit()
            display.stop()
            vdisplay.stop()

        driver.save_screenshot('happybirthday-begin-{}.{}'.format(c_user.strip(), 'png'))
        helper.happy_birthday(driver, "Chúc mừng sinh nhật !")
    except Exception as e:
        print(e)
    finally:
        driver.quit()
        display.stop()
        vdisplay.stop()

