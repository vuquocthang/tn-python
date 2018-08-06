import helper
import requests
#from pyvirtualdisplay import Display
import time
#from xvfbwrapper import Xvfb
import datetime

#url = "http://toolnuoi999.tk"
url = "http://192.168.81.139:8001"
image_path = "/home/toolnuoi999.tk/source/storage/app/post"

while True:
    print("=====================Log======================")

    # get post
    post = requests.get("{}/api/post".format(url)).json()

    now = datetime.datetime.now()

    try:
        if(  str(now.hour) == str(post['time']) ):
            print(" Hour : {}".format(now.hour))

            # init display
            #vdisplay = Xvfb()
            #vdisplay.start()
            #display = Display(visible=0, size=(800, 600))
            #display.start()

            # init driver
            driver = helper._init( post['clone']['ip'], post['clone']['port'], post['clone']['c_user'], post['clone']['xs'])

            try:
                # files
                files = post['files']

                # image path
                imagepaths = []

                #for file in files:
                    #imagepaths.append("{}/{}".format(image_path, file['filename']))

                # post
                helper.post_status(driver, post['text'], imagepaths)

            except Exception as e:
                print("Ex1 : {}".format(e))
                driver.save_screenshot('post-{}.{}'.format( post['clone']['c_user'], 'png'))
                driver.quit()
                #display.stop()
                #vdisplay.stop()
            else:
                driver.save_screenshot('post-{}.{}'.format( post['clone']['c_user'], 'png'))
                driver.quit()

                requests.post("{}/api/posted".format(url) , {
                    'post_id' : post['id']
                })
                #display.stop()
                #vdisplay.stop()
        else:
            time.sleep(5)
    except:
        time.sleep(5)