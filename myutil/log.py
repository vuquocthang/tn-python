import requests
import os

api_url = "http://toolnuoi999.tk"
#api_url = "http://192.168.81.139:8001/"

#params
# chanel = { 'chat', 'post', 'happybirthday' }
# content : string
import helper

def save(channel, content):
    try:
        url = "{}/api/log".format(api_url)

        requests.post(url, {
            'type'      : channel,
            'content'   : content,
            'api_key'   : helper.get_api_key()
        })
    except Exception as e:
        return e

def save_image_log(driver, name, path):
    driver.save_screenshot(os.path.join(path, name))


#test
save('happybirthday', 'foo')