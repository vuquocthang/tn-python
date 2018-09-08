import helper
import requests
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
    schedules = requests.get("{}/api/schedule".format(url), {
        'api_key': helper.get_api_key()
    }).json()

    now = datetime.datetime.now()

    for schedule in schedules:
        if (str(now.hour) == str(schedule['hour'])):

            print(" Hour : {}".format(now.hour))
            logging.info("Perform schedule : {}".format(schedule['id']))

            clones = schedule['clones']

            for clone in clones:
                driver = None

                try:
                    # init driver
                    driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                    check = myutil.init._is_checkpoint(driver, clone)

                    if check is False:
                        print("Clone is checkpoint")
                        driver.quit()
                        break

                    print("Driver : ".format(driver))

                    # image path
                    imagepaths = []

                    # post
                    helper.post_status(driver, schedule['post']['text'], imagepaths)

                    print("Post status successfully")

                    requests.post("{}/api/schedule/performed".format(url), {
                        'post_cat_schedule_id': schedule['id'],
                        'api_key': helper.get_api_key()
                    })

                    driver.quit()

                except Exception as e:
                    print("Exception init : {}".format(e))
                    print(driver)

                    driver.quit()
                finally:
                    driver.quit()

        else:
            time.sleep(5)
