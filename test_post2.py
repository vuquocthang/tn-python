import helper
import requests
from pyvirtualdisplay import Display
import time
from xvfbwrapper import Xvfb



url = "http://toolnuoi999.tk"
image_path = "/home/toolnuoi999.tk/source/storage/app/post"

while True:
    try:
        print("=====================Log======================")

        #get clone
        clone = requests.get("{}/api/clone".format(url)).json()

        #init display
        vdisplay = Xvfb()
        vdisplay.start()
        display = Display(visible=0, size=(800, 600))
        display.start()

        #init driver
        driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])

        try:
            #get post
            post = requests.get("{}/api/post".format(url)).json()

            #files
            files = post['files']

            #image path
            imagepaths = []

            for file in files:
                imagepaths.append( "{}/{}".format(image_path, file['filename']) )

            #post
            helper.post_status(driver, post['text'] , imagepaths)

        except Exception as e:
            print("Ex1 : {}".format(e) )
            driver.save_screenshot('post-{}.{}'.format(clone['c_user'], 'png'))
            driver.quit()
            display.stop()
            vdisplay.stop()
        else:
            driver.save_screenshot('post-{}.{}'.format(clone['c_user'], 'png'))
            driver.quit()
            display.stop()
            vdisplay.stop()
    except Exception as e:
        print(e)
        time.sleep(60)
    else:
        break