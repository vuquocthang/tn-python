import helper
from pyvirtualdisplay import Display

c_user = "100025897411907"
xs = "19%3ABe_U9Sr2-bQ89A%3A2%3A1525300962%3A-1%3A-1"
ip = "5.104.176.199"
port = 1080

display = Display(visible=0, size=(800, 600))
display.start()
driver = helper._init(ip, port, c_user, xs)
driver.quit()
display.stop()
