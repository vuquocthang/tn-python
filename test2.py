import helper
from pyvirtualdisplay import Display
import datetime
import util.init

'''
c_user = "100025897411907"
xs = "19%3ABe_U9Sr2-bQ89A%3A2%3A1525300962%3A-1%3A-1"
ip = "103.15.51.160"
port = 8080
'''

'''
c_user = "100026833845829"
xs = "43%3AYdCSncXZq_Ls5g%3A2%3A1531509655%3A12946%3A9970"
ip = "123.30.172.60"
port = 3128
'''

'''
c_user = "100025349360731"
xs = "39%3AXdm3-dStQLlrYQ%3A2%3A1523736783%3A-1%3A-1"
ip = "103.228.118.238"
port = 8080
'''

'''
c_user = "100027507696104"
xs = "35:mNxG9iS8Xt83aQ:2:1531757851:-1:-1"
ip = "180.148.4.194"
port = 8080
'''

#driver = helper._init(ip, port, c_user, xs)
#driver.get("https://www.facebook.com/")

#driver = helper._init(ip, port, c_user, xs)

#helper.rep_comment(driver, c_user)
#print( helper.rep_comment(driver, c_user) )

#helper.accept_friend(driver)
#driver.quit()
#display.stop()

c_user = "100025897411907"
xs = "19%3ABe_U9Sr2-bQ89A%3A2%3A1525300962%3A-1%3A-1"
ip = "93.170.131.97"
port = 21169

#display = Display(visible=0, size=(800, 600))
#display.start()
driver = helper._init(ip, port, c_user, xs)
driver.get("https://www.facebook.com")

#driver.quit()
#display.stop()
