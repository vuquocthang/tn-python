import helper
import requests
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb
import random
from random import choice
import time

url = "http://toolnuoi999.tk/api/clones"
useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"

clones = requests.get(url).json()

for clone in clones:

    print(clone)

    # init display
    vdisplay = Xvfb()
    vdisplay.start()
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = None

    try:
        driver = helper._init_with_useragent(clone['ip'], clone['port'], clone['c_user'], clone['xs'], useragent)

        helper.react_post_in_newfeeds(driver, random.choice([2, 3, 4, 5, 6]))
        helper.react_post_in_newfeeds(driver, random.choice([2, 3, 4, 5, 6]))
        helper.react_post_in_newfeeds(driver, random.choice([2, 3, 4, 5, 6]))
        helper.react_post_in_newfeeds(driver, random.choice([2, 3, 4, 5, 6]))
        helper.react_post_in_newfeeds(driver, random.choice([2, 3, 4, 5, 6]))

        time.sleep(5)

    except Exception as e:
        print(e)
        if driver is not None:
            driver.quit()
    else:
        try:
            driver.quit()
        except Exception as e:
            print(e)
    display.stop()
    vdisplay.stop()

