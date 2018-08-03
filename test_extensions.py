import helper
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()
display = Display(visible=0, size=(800, 600))
display.start()

helper._init_with_extension()

driver.save_screenshot("test-extensions.png")

driver.quit()
display.stop()
vdisplay.stop()