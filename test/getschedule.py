import requests

url = "http://toolnuoi999.tk"

schedules = requests.get("{}/api/schedule".format(url)).json()


for schedule in schedules:
    print(schedule['id'])

    print(schedule['post']['files'])
