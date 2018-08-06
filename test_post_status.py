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