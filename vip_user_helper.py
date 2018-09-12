import helper

def get_message_from_keyword(keywords, message, name):
    if len(keywords) == 0:
        return False

    for k in keywords:
        if k['key'].lower() in message.lower():
            return k['value'].replace("[name]", name)

    return False

def newest_message(driver, keywords):
    try:
        driver.get("https://m.facebook.com/messages/?folder=unread")

        conversations = driver.find_elements_by_xpath("//div[@id='root']//tbody//a[contains(@href,'/messages/read')]")

        if (len(conversations) == 0):
            return 0

        links = []

        for conversation in conversations:
            link = conversation.get_attribute('href')
            links.append(link)

        for link in links:
            try:
                print(link)
                driver.get(link)
                recipient_message = driver.find_element_by_xpath("//div[@id='fua']//span[1]").text
                recipient_name = driver.find_element_by_xpath("//div[@id='fua']//strong[1]").text

                message = get_message_from_keyword(keywords, recipient_message, recipient_name)

                #print(message)

                if message is not False:
                    print(message)
                    helper.send_message(driver, link, message)
                else:
                    print("Message not has keyword")
            except Exception as e:
                print(e)
    except Exception as e:
        return "error : {}".format(e)
    else:
        return True

def request_message(driver, keywords):
    try:
        driver.get("https://m.facebook.com/messages/?folder=pending")

        conversations = driver.find_elements_by_xpath("//div[@id='root']//tbody//a[contains(@href,'/messages/read')]")

        if (len(conversations) == 0):
            return 0

        links = []

        for conversation in conversations:
            link = conversation.get_attribute('href')

            links.append(link)

        for link in links:
            try:
                print(link)
                driver.get(link)
                # send_message(driver, link, "This is a virus" )

                recipient_message = driver.find_element_by_xpath("//div[@id='fua']//span[1]").text
                recipient_name = driver.find_element_by_xpath("//div[@id='fua']//strong[1]").text

                message = get_message_from_keyword(keywords, recipient_message, recipient_name)

                #print(message)

                if message is not False:
                    helper.send_message(driver, link, message)
                else:
                    print("Message not has keyword")
            except Exception as e:
                print(e)

    except Exception as e:
        return "error : {}".format(e)
    else:
        return True

