from pyvirtualdisplay import Display
import datetime
import myutil.init
#from xvfbwrapper import Xvfb
import os


print( os.path.join( os.path.dirname(__file__), "") )

c_user = "100011668026584"
xs = "18%3AZdcoMMLdjrt1CA%3A2%3A1534915763%3A16846%3A6347"
ip = "93.170.131.97"
port = 21169

driver = myutil.init._init(ip, port, c_user, xs)
driver.get("https://www.facebook.com")

