from flask import Flask, request, jsonify
app = Flask(__name__)
import json
import time
from pyvirtualdisplay import Display
import helper

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


if __name__ == '__main__':
   app.run(host='0.0.0.0')