from pyvirtualdisplay import Display
import datetime
from xvfbwrapper import Xvfb
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
import init

c_user = "100011668026584"
xs = "12%3AH-Hccg_y1Y99wg%3A2%3A1534733997%3A16846%3A6347"
ip = "93.170.131.97"
port = 21169

vdisplay = Xvfb()
vdisplay.start()
display = Display(visible=0, size=(800, 600))
display.start()
driver = init._init(ip, port, c_user, xs)
driver.get("https://www.facebook.com")
driver.save_screenshot("fb.png")

vdisplay.stop()
display.stop()
