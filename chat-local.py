import helper
import requests
import threading
import time
import myutil.init
import myutil.log as mylog

url = "http://toolnuoi999.tk"

NUM_WORKERS = 1

def create_workers():
    for x in range(NUM_WORKERS):
        t = threading.Thread(target=work)
        #t.daemon = True
        t.start()

def work():
    while True:
        try:
            '''
            clone = requests.get("{}/api/clone/Live".format(url),{
                'api_key' : helper.get_api_key()
            }).json()
            '''
            clone = requests.get("{}/api/clone/Live".format(url)).json()

            if clone is None:
                break
            mylog.save("chat", str(clone['uid']))
            driver = None

            try:
                driver = myutil.init._init(clone['ip'], clone['port'], clone['c_user'], clone['xs'])
                check = myutil.init._is_checkpoint(driver, clone)

                if check is False:
                    print("Clone is checkpoint")
                    mylog.save("chat", "Clone is checkpoint")
                    driver.quit()
                    #break
                else:
                    helper.newest_message(driver)
                    helper.request_message(driver)

                    #active_user_links = helper.active_conversations(driver)
                    #helper.message_to_active_users(driver, active_user_links)
            except Exception as e:
                print("Exception : {}".format(e))
                mylog.save("chat", str(e))

                driver.quit()
            finally:
                driver.quit()

        except Exception as e:
            print(e)

        time.sleep(5)

create_workers()

