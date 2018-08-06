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
                    driver = helper._init( clone['ip'], clone['port'], clone['c_user'], clone['xs'])

                    try:
                        # files
                        files = schedule['post']['files']

                        # image path
                        imagepaths = []

                        for file in files:
                            imagepaths.append("{}/{}".format(image_path, file['filename']))

                        # post
                        helper.post_status(driver, schedule['post']['text'], imagepaths)

                    except Exception as e:
                        print("Exception : {}".format(e))

                        driver.save_screenshot(
                            os.path.join(logging_path, 'post-exception-{}.{}'.format(clone['c_user'], 'png'))
                        )

                        driver.quit()
                        display.stop()
                        vdisplay.stop()
                    else:
                        print("Post status successfully")

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
    except Exception as e:
        print("Ex : {}".format(e))
        time.sleep(5)
