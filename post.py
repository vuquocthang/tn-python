import helper
import requests
from pyvirtualdisplay import Display
import time
from xvfbwrapper import Xvfb
import datetime
import logging
import sys, os
logging.basicConfig(filename='post.log',level=logging.DEBUG)

url = "http://toolnuoi999.tk"
image_path = "/home/toolnuoi999.tk/source/storage/app/post"

logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-post-logging')

while True:
    logging.info("Perform : {}".format(datetime.datetime.now()) )
    #print("=====================Log======================")

    # get schedules
    schedules = requests.get("{}/api/schedule".format(url)).json()

    now = datetime.datetime.now()

    try:
        for schedule in schedules:
            if(  str(now.hour) == str(schedule['hour']) ):

                print(" Hour : {}".format(now.hour))
                logging.info("Perform schedule : {}".format(schedule['id']))

                clones = schedule['clones']

                for clone in clones:
                    # init display
                    vdisplay = Xvfb()
                    vdisplay.start()
                    display = Display(visible=0, size=(800, 600))
                    display.start()

                    # init driver
                    useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
                    driver = helper._init_with_useragent(clone['ip'], clone['port'], clone['c_user'], clone['xs'], useragent)
                    driver.get("https://facebook.com")

                    driver.save_screenshot("init.png")

                    try:
                        # files
                        files = schedule['post']['files']

                        # image path
                        image_paths = []
                        for file in files:
                            image_paths.append("{}/{}".format(image_path, file['filename']))

                        # post
                        helper.post_status2(driver, schedule['post']['text'], image_paths)

                    except Exception as e:
                        print("Ex1 : {}".format(e))

                        driver.save_screenshot(
                            os.path.join(logging_path, 'post-exception-{}.{}'.format(clone['c_user'], 'png'))
                        )

                        driver.quit()
                        display.stop()
                        vdisplay.stop()
                    else:

                        driver.save_screenshot(
                            os.path.join(logging_path, 'post-success-{}.{}'.format(clone['c_user'], 'png'))
                        )

                        requests.post("{}/api/schedule/performed".format(url) , {
                            'post_cat_schedule_id' : schedule['id']
                        })

                        driver.quit()
                        display.stop()
                        vdisplay.stop()
            else:
                time.sleep(5)
    except:
        time.sleep(5)
