from selenium import webdriver
import time
import InstaFunc
import InstaStrategy

driver = InstaFunc.login("account@instagram.de", "accountpassword")

# You will see this quite regularly in the script - in order to reduce danger of bans the script waits a certain amount of time before doing anything.
time.sleep(5)

# These are some examples for using the crawler, for instance liking 5 posts with the hashtag "NHL".

driver = InstaStrategy.likechain(driver, "nhl", 5)
#driver = InstaStrategy.followchain(driver, "diaet", 100)
#InstaFunc.followers(driver, "https://www.instagram.com/tomtomkk6/")
#InstaFunc.writeactivity(driver, "test", "test", "test")
#driver = InstaStrategy.unfollow(driver)

InstaFunc.closeactivities()
input("Beenden?")
driver.close()
driver.quit()