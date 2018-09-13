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



def rep_comment_on_mobile(driver, uid, keywords):
    driver.get("https://m.facebook.com/{}".format(uid))
    articles = driver.find_elements_by_xpath("//div[@id='structured_composer_async_container']/div[1]/div")

    comment_links = []

    for index, article in enumerate(articles):
        try:
            link = driver.find_element_by_xpath("//div[@id='structured_composer_async_container']/div[1]/div[{}]//a[contains(@href, 'story.php')]".format(index + 1)).get_attribute("href")
            comment_links.append( link )
            print( link )
        except Exception as e:
            link = driver.find_element_by_xpath(
                "//div[@id='structured_composer_async_container']/div[1]/div[{}]//a[contains(@href, 'photo.php')]".format(
                    index + 1)).get_attribute("href")
            comment_links.append(link)
            print(link)
            print(e)


    for link in comment_links:
        try:
            print(link)
            driver.get(link)
            comment_items = driver.find_elements_by_xpath("//div[@id='m_story_permalink_view']/div[2]/div[1]/div[4]/div")


            print("comments : {}".format(len(comment_items)))

            for index, item in enumerate(comment_items):
                try:
                    driver.get(link)
                    comment = driver.find_element_by_xpath("//div[@id='m_story_permalink_view']/div[2]/div[1]/div[4]/div[{}]".format(index + 1)).text

                    print(comment)

                    if ('You replied' not in comment) and ('Bạn đã trả lời' not in comment ) and ('Bạn đã phản hồi' not in comment):
                        message = get_message_from_keyword(keywords, comment, "")

                        if message is not False:
                            driver.find_element_by_xpath("//div[@id='m_story_permalink_view']/div[2]/div[1]/div[4]/div[{}]/div[1]/div[3]/a[1]".format(index + 1)).click()
                            driver.find_element_by_id("composerInput").send_keys(message)
                            driver.find_element_by_xpath("//*[@type='submit']").click()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)