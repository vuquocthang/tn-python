import helper
import requests
import time
import datetime
import logging
import os
import myutil.init
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb
import myutil.log as mylog

#logging.basicConfig(filename='post.log',level=logging.DEBUG)
url = "http://toolnuoi999.tk"
image_path = "/home/toolnuoi999.tk/source/storage/app/post"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-post-logging')

while True:
    schedules = requests.get("{}/api/schedule".format(url),{
                'api_key' : helper.get_api_key()
            }).json()

    now = datetime.datetime.now()

    for schedule in schedules:
        if (str(now.hour) == str(schedule['hour'])):

            print(" Hour : {}".format(now.hour))
            #logging.info("Perform schedule : {}".format(schedule['id']))

            clones = schedule['clones']

            for clone in clones:
                mylog.save("post", "Clone uid : {}".format(clone['c_user']))
                driver = None

                # init driver
                vdisplay = Xvfb()
                vdisplay.start()
                display = Display(visible=0, size=(800, 600))
                display.start()

                try:
                    driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                    check = myutil.init._is_checkpoint(driver, clone)

                    print("Check checkpoint : {}".format(check))

                    if check is False:
                        print("Clone is checkpoint")
                        driver.quit()
                        break

                    print("Driver is None: {}".format(driver is None))

                    # files
                    files = schedule['post']['files']

                    # image path
                    imagepaths = []

                    for file in files:
                        imagepaths.append("{}/{}".format(image_path, file['filename']))

                    print("Image paths : {}".format(imagepaths))

                    # post
                    helper.post_status(driver, schedule['post']['text'], imagepaths)

                    # success
                    print("Post status successfully")
                    mylog.save("post", "Post clone uid {} successfully".format(clone['c_user']))

                    driver.save_screenshot(
                        os.path.join(logging_path, 'post-success-{}.{}'.format(clone['c_user'], 'png'))
                    )

                    requests.post("{}/api/schedule/performed".format(url), {
                        'post_cat_schedule_id': schedule['id'],
                        'api_key': helper.get_api_key()
                    })
                    driver.quit()

                except Exception as e:
                    print("Exception init : {}".format(e))
                    mylog.save("post", "Post ex : {}".format(e))

                    driver.save_screenshot(
                        os.path.join(logging_path, 'post-exception-{}.{}'.format(clone['c_user'], 'png'))
                    )
                    driver.quit()
                else:
                    print("Done")
                    driver.quit()

                display.stop()
                vdisplay.stop()

        else:
            time.sleep(5)
