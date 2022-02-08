from selenium import webdriver
import time
import csv
import InstaFunc
import random


# Likes a specified number of posts on a given hashtag #
def likechain(driver, search_hashtag, iterations):

    counter = 0
    strategy = "likechain"

    link = "https://www.instagram.com/explore/tags/" + str(search_hashtag)
    driver.get(link)
    time.sleep(5)
    driver.find_elements_by_xpath("//article/div[2]/div/div[1]/div[1]/a/div")[0].click()

    while counter < iterations:
        try:
            InstaFunc.actionlike(driver, search_hashtag, strategy)
            driver.find_elements_by_xpath("//html/body/div[2]/div/div[1]/div/div/a[2]")[0].click()
            time.sleep(2)
        except:
            break
        counter = counter + 1
    return driver


# Follows a specified number of users who posted on a given hashtag #
def followchain(driver, search_hashtag, iterations):

    counter = 0
    strategy = "followchain"

    link = "https://www.instagram.com/explore/tags/" + str(search_hashtag)
    driver.get(link)
    time.sleep(5)
    driver.find_elements_by_xpath("//article/div[2]/div/div[1]/div[1]/a/div")[0].click()

    while counter < iterations:
        try:
            InstaFunc.actionfollow(driver, search_hashtag, strategy)
            time.sleep(2)
            driver.find_elements_by_xpath("//html/body/div[2]/div/div[1]/div/div/a[2]")[0].click()
            time.sleep(2)
        except:
            break
        counter = counter + 1
    return driver

# Defollow a number a list of accounts given in a .csv file. #
def unfollow(driver):

    with open("defollow.csv", newline='') as file:

        for line in file:
            data = line.strip().split(";")
            link = data[2]

            driver.get(link)
            time.sleep(2)

            try:
                InstaFunc.defollow(driver)
            except:
                continue

    return driver
