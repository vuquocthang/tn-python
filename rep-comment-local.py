import helper
import requests
import time
import datetime
import logging
import sys, os
import myutil.init

'''

logging.basicConfig(filename='post.log',level=logging.DEBUG)


c_user = "100013630568585"
xs = "23%3Al22zV0krm2j-og%3A2%3A1535095915%3A17613%3A6145"
ip = "109.248.222.168"
port = "33423"

driver = myutil.init._init(ip, port, c_user, xs)
helper.rep_comment_on_mobile(driver, c_user)
'''

import env

print(env.KEY['API'])
print(helper.get_api_key())