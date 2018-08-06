from flask import Flask, request, jsonify
app = Flask(__name__)
import json
import time
from pyvirtualdisplay import Display
import helper
from xvfbwrapper import Xvfb
import requests

api_url = "http://toolnuoi999.tk/api"

@app.route('/')
def index():
    return 'Hmm , Hello '

@app.route('/get-params', methods = ['POST'])
def params():
    if request.method == 'POST':
        uids = json.loads(request.form['uids'])
        print( uids )

    return 'Done'

@app.route('/add-friend', methods = ['POST'])
def add_friend():
    if request.method == 'POST':
        clone = json.loads(request.form['clone'])
        print(clone)

        ip = clone['ip']
        port = clone['port']
        c_user = clone['c_user']
        xs = clone['xs']

<<<<<<< HEAD
        driver = helper._init(ip, port, c_user, xs)

        for uid in clone['uids']:
            try:
                print(uid['uid'])
                helper.add_friend(driver, uid['uid'])
            except Exception as e:
                print(e)
            time.sleep(3)

        driver.quit()
    return 'Done'

@app.route('/post-status', methods = ['POST'])
def post():
    if request.method == 'POST':
        clone = json.loads(request.form['clone'])
        print(clone)

        data = json.loads(request.form['data'])
        print(data)

        ip = clone['ip']
        port = clone['port']
        c_user = clone['c_user']
        xs = clone['xs']

        text = data[0]['text']
        imagePaths = []
        basepath = "home/toolnuoi.com/source/storage/app/post/"

        for item in data:
            imagePaths.append( basepath + item['filename'])

        display = Display(visible=0, size=(800, 600))
        display.start()

        driver = helper._init(ip, port, c_user, xs)
        helper.post_status(driver, text, imagePaths)

        driver.quit()
        display.stop()

    return 'Done'


=======
        try:
            vdisplay = Xvfb()
            vdisplay.start()
            display = Display(visible=0, size=(800, 600))
            display.start()
            driver = helper._init(ip, port, c_user, xs)
            driver.save_screenshot('add-begin-{}.{}'.format(c_user.strip(), 'png'))

            for uid in clone['uids']:
                try:
                    print(uid['uid'])
                    helper.add_friend(driver, uid['uid'])

                    # post to server
                    requests.post("{}/{}".format(api_url, "addfriend"), {
                        'clone_id': clone['id'],
                        'uid': uid['uid']
                    })

                    driver.save_screenshot('adddone-{}-{}.{}'.format(uid['uid'].strip(), c_user.strip(), 'png'))
                except Exception as e:

                    # post to server
                    requests.post("{}/{}".format(api_url, "addfriend"), {
                        'clone_id': clone['id'],
                        'uid': uid['uid']
                    })
                    
                    print(e)
                    driver.save_screenshot('addex-{}-{}.{}'.format( uid['uid'].strip(), c_user.strip() , 'png'))


                time.sleep(3)
            driver.quit()
            display.stop()
            vdisplay.stop()
        except Exception as e:
            print(e)
    return 'Done'

>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624
if __name__ == '__main__':
   app.run(host='0.0.0.0')
