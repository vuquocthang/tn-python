from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://booking.kayak.com/flights/TXL-SVO/2018-06-26?sort=bestflight_a")
driver.save_screenshot("booking.png")