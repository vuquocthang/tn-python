import helper
import requests
import time
import datetime
import logging
import sys, os
import myutil.init

logging.basicConfig(filename='post.log',level=logging.DEBUG)


c_user = "100025142415320"
xs = "15%3A06KJW5UZ-yG22Q%3A2%3A1535369020%3A-1%3A5387"
ip = "185.135.80.3"
port = "21169"

driver = myutil.init._init(ip, port, c_user, xs)
helper.rep_comment_on_mobile(driver, c_user)