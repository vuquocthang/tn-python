<<<<<<< HEAD
import helper
import requests

'''
c_user = "100022858866847"
xs = "12%3Al1bUt0KdDPlLlQ%3A2%3A1530805049%3A15356%3A7153"
ip = "180.250.5.36"
port = "8080"

driver = helper._init(ip, port, c_user, xs)
'''



url = "http://toolnuoi999.tk"

clone = requests.get("{}/api/clone".format(url)).json()
driver = helper._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])


post = requests.get("{}/api/post".format(url)).json()

print( post['clones'] )

Imagepath = [
    #"/home/toolnuoi999.tk/python/log-100025827095902.png",
    #"/home/toolnuoi999.tk/python/log-100025827095902.png",
    #"/home/toolnuoi999.tk/python/log-100025827095902.png"
]


helper.post_status2(driver, post['text'] , Imagepath)
=======
# coding=utf-8

import helper

import requests

from pyvirtualdisplay import Display


url = "http://toolnuoi999.tk/api/post"
post = requests.get(url).json()


#c_user = "100022858866847"

#xs = "12%3Al1bUt0KdDPlLlQ%3A2%3A1530805049%3A15356%3A7153"

#ip = "180.250.5.36"

#port = "8080"


c_user 	= post["clones"][0]["c_user"]
xs 	= post["clones"][0]["xs"]
ip 	= post["clones"][0]["ip"]
port 	= post["clones"][0]["port"]


display = Display(visible=0, size=(800, 600))

display.start()

driver = helper._init(ip, port, c_user, xs)











print( post['clones'] )



Imagepath = []


image_base_path = "/home/toolnuoi999.tk/source/storage/app/post/{}"

for file in post['files']:
	Imagepath.append( image_base_path.format(file['filename']) )


print(Imagepath)


helper.post_status(driver, post['text'] , Imagepath)



driver.quit()

display.stop()
>>>>>>> fe45538839ec3ad19d0d3f68e6f16e124e7e4624
