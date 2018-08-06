import helper

useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"

ip = "93.170.131.97"
port = "21169"
c_user = "100011668026584"
xs = "2%3Am9V7CKveVOXaCA%3A2%3A1533460435%3A16846%3A6347"

driver = helper._init_with_useragent(ip, port, c_user, xs, useragent)

driver.get("https://facebook.com")

image_paths = [
    "E:\myproject\message\image\eWtfMME.png",
    'E:\myproject\message\image\q.jpg'
]

helper.post_status2(driver, "Test auto post", image_paths)