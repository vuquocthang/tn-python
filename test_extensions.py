import helper
import time
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb

ip = "93.170.128.201"
port = "21169"
username = "hohzaipa"
password = "Em4q6QYK"

vdisplay = Xvfb()
vdisplay.start()
display = Display(visible=0, size=(800, 600))
display.start()

driver = helper._init_with_extension()

driver.save_screenshot("extension.png")

time.sleep(2)

driver.find_element_by_class_name("button").click()
driver.find_element_by_xpath("//*[@id='mode']//option[2]").click()

driver.find_elements_by_class_name("show-for-medium")[0].click()
driver.find_element_by_xpath("//*[@id='newProxyType']/option[@value=3]").click()

driver.find_element_by_id("newProxyAddress").send_keys(ip)
driver.find_element_by_id("newProxyPort").send_keys(port)
driver.find_element_by_id("newProxyUsername").send_keys(username)
driver.find_element_by_id("newProxyPassword").send_keys(password)

driver.find_element_by_id("newProxySave").click()

driver.get("https://api.ipify.org/?format=json")

driver.save_screenshot("ip.png")

driver.quit()
display.stop()
vdisplay.stop()