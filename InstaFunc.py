from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

ActivitiesNew = []

class activity():

    def __init__(self, timestamp, account, post, source, strategy, type, content):
        self.timestamp = timestamp #Uhrzeit der Aktivität#
        self.account = account #Account#
        self.post = post
        self.source = source #Hashtag
        self.strategy = strategy #Strat
        self.type = type #Typ der Aktivität: Like/Comment/Follow/Defollow#
        self.content = content

class follower():

    def __init__(self, link):
        self.link = link
        #self.follow = follow

### CORE FUNCTIONS ###
def login(username, password):

    # Loading the webdriver, which needs to be available locally. Then Instagram's loginpage is loaded.#
    driver = webdriver.Chrome("C:\Program Files\BrowserDriver\chromedriver.exe")
    driver.set_page_load_timeout(20)
    driver.get("http:\\www.instagram.com/accounts/login")
    time.sleep(3)

    # Entering username and password #
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(u'\ue007')

    return driver


# Like a post #
def like(driver):

    driver.find_elements_by_xpath("//span[@aria-label='Gefällt mir']")[0].click()

    return driver

# Comment a post#
def comment(driver, text):

    driver.find_elements_by_xpath('//textarea[@placeholder = "Kommentar hinzufügen ..."]')[0].clear()
    driver.find_elements_by_xpath('//textarea[@placeholder = "Kommentar hinzufügen ..."]')[0].send_keys(text)
    driver.find_elements_by_xpath('//textarea[@placeholder = "Kommentar hinzufügen ..."]')[0].send_keys(u'\ue007')

    return driver

# Follow a user'
def follow(driver):

    driver.find_elements_by_xpath("//button[contains(text(),'Folgen')]")[0].click()

    return driver

# Defollow a user'
def defollow(driver):

    driver.find_elements_by_xpath("//button[contains(text(),'Abonniert')]")[0].click()
    time.sleep(1)
    driver.find_elements_by_xpath("//button[contains(text(),'Nicht mehr folgen')]")[0].click()

    return driver

# Log all activities as a class activity #
def writeactivity(driver, search_hashtag, search_strategy, activity_type):

    timestamp = time.time()
    account = driver.find_elements_by_xpath("//article/header/div[2]/div[1]/div[1]/h2/a")[0].get_attribute("href")
    post = driver.current_url
    source = search_hashtag
    strategy = search_strategy
    content = 0
    type = activity_type

    f = activity(timestamp, account, post, source, strategy, type, content)
    ActivitiesNew.append(f)

    return driver

### ACTION ANCHOR MIT ACTIVITIES ###

def actionlike(driver, search_hashtag, search_strategy):

    checkrandom = wait()
    if checkrandom == 1:
        like(driver)
        writeactivity(driver, search_hashtag, search_strategy, "like")

    return driver

### APPENDIX ###

# To reduce risks of ban, for each activity there is a 20% chance that the particular post is skipped. Also, the bot waits up to 5 seconds before proceeding with the next activity. #
def wait():

    waittime = round(random.uniform(2, 5), 3)
    time.sleep(waittime)
    checkpass = random.uniform(1, 10)
    if checkpass <= 8:
        return 1
    else:
        return 0


# Save all activities in a .csv log #
def closeactivities():

    with open('activities.csv', 'a', newline='') as file:
        rowwriter = csv.writer(file, delimiter=';', quotechar='"')
        for items in ActivitiesNew:
            rowwriter.writerow([items.timestamp] + [items.account] + [items.post] + [items.source] + [items.strategy] + [items.type] + [items.content])

# Get a list of all followers of a certain account #
def followers(driver, link):

    ListFollower = []
    driver.get(link)
    time.sleep(5)

    driver.find_elements_by_xpath("//section/main/div/header/section/ul/li[2]/a")[0].click()
    time.sleep(5)
    k = 1
    while True:
        time.sleep(2)
        items = driver.find_elements_by_xpath("//div/div[1]/div/div[1]/a")
        print(items)
        length_old = len(items)

        
        time.sleep(0.5)
        items = driver.find_elements_by_xpath("//div/div[1]/div/div[1]/a")
        length_new = len(items)

        k = k + 1

        if length_old == length_new:
            break

    a = 1
    for item in items:
        a = a + 1
        if a > 7:
            link = item.get_attribute("href")
            f = follower(link)
            ListFollower.append(f)

    with open('followerscrape.csv', 'w', newline='') as file:
        rowwriter = csv.writer(file, delimiter=';', quotechar='"')
        for items in ListFollower:
            rowwriter.writerow([items.link])

    return driver