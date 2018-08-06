import helper
import time

ip = "78.153.149.57"
port = "21169"
username = "hohzaipa"
password = "Em4q6QYK"

'''
driver = helper._init_with_extension(ip, port)
driver.get("https://api.ipify.org/?format=json")

driver.save_screenshot("ip.png")
'''

driver = helper._init(ip, port, "a", "b")