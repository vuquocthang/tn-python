import helper
import requests
import time
import datetime
import logging
import sys, os
import myutil.init

logging.basicConfig(filename='post.log',level=logging.DEBUG)


c_user = "100025142415320"
xs = "15%3AcRuEsdD_V7kd2A%3A2%3A1536185214%3A2480%3A6258"
ip = "109.248.222.168"
port = "33423"

driver = myutil.init._init(ip, port, c_user, xs)
helper.rep_comment_on_mobile(driver, c_user)