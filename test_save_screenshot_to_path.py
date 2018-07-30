from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.firefox.options import Options
import os
import sys
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pyvirtualdisplay import Display
import time
from xvfbwrapper import Xvfb


vdisplay = Xvfb()
vdisplay.start()
display = Display(visible=0, size=(800, 600))
display.start()

firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
# firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = 'geckodriver.exe'
firefox_capabilities['acceptInsecureCerts'] = True
firefox_capabilities['acceptUntrustedCertificates'] = True
firefox_capabilities['assumeUntrustedCertificateIssuer'] = True
firefox_capabilities['acceptNextAlert'] = True

fp = webdriver.FirefoxProfile()
fp.accept_untrusted_certs = True
fp.assume_untrusted_cert_issuer = True
# fp.setAcceptUntrustedCertificates = True
# fp.setAssumeUntrustedCertificateIssuer = False
fp.accept_next_alert = True
#fp.set_preference('permissions.default.image', 2)
#fp.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# fp.set_preference("general.useragent.override", random.choice(useragents))

fp.update_preferences()

options = Options()
# options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=options, firefox_profile=fp, capabilities=firefox_capabilities)
driver.get("https://page5s.com")

print (os.path.abspath())

path = os.path.join( os.path.abspath(), 'image_logging', 'p.png' )

driver.save_screenshot(path)

driver.quit()
display.stop()
vdisplay.stop()