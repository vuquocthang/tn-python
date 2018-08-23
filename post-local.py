import helper
import requests
#from pyvirtualdisplay import Display
#from xvfbwrapper import Xvfb
import time
import datetime
import logging
import sys, os
import myutil.init

logging.basicConfig(filename='post.log',level=logging.DEBUG)

url = "http://toolnuoi999.tk"
image_path = "/home/toolnuoi999.tk/source/storage/app/post"
logging_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'image-post-logging')

while True:
    schedules = requests.get("{}/api/schedule".format(url)).json()

    now = datetime.datetime.now()

    for schedule in schedules:
        if (str(now.hour) == str(schedule['hour'])):

            print(" Hour : {}".format(now.hour))
            logging.info("Perform schedule : {}".format(schedule['id']))

            clones = schedule['clones']

            for clone in clones:

                # init display
                #vdisplay = Xvfb()
                #vdisplay.start()
                #display = Display(visible=0, size=(800, 600))
                #display.start()

                driver = None

                try:
                    # init driver
                    driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                    check = myutil.init._is_checkpoint(driver, clone)

                    if check is False:
                        print("Clone is checkpoint")
                        driver.quit()
                        #display.stop()
                        #vdisplay.stop()
                        break

                except Exception as e:
                    print("Ex init : {}".format(e))

                    if driver is not None:
                        try:
                            driver.quit()
                            #display.stop()
                            #vdisplay.stop()
                        except Exception as e:
                            print(e)
                else:

                    try:
                        # files
                        files = schedule['post']['files']

                        # image path
                        imagepaths = []

                        # for file in files:
                        # imagepaths.append("{}/{}".format(image_path, file['filename']))

                        # post
                        helper.post_status(driver, schedule['post']['text'], imagepaths)

                    except Exception as e:
                        print("Exception 1 : {}".format(e))

                        driver.save_screenshot(
                            os.path.join(logging_path, 'post-exception-{}.{}'.format(clone['c_user'], 'png'))
                        )

                    else:
                        print("Post status successfully")

                        driver.save_screenshot(
                            os.path.join(logging_path, 'post-success-{}.{}'.format(clone['c_user'], 'png'))
                        )

                        requests.post("{}/api/schedule/performed".format(url), {
                            'post_cat_schedule_id': schedule['id']
                        })

                if driver is not None:
                    try:
                        driver.quit()
                    except Exception as e:
                        print("Ex 2 : {}".format(e))

                #display.stop()
                #vdisplay.stop()
        else:
            time.sleep(5)
