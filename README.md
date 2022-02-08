### Overview

This project is a case study to simulate an Instagram Bot, trying to mimic the natural engagement of a user in the desktop browser and doing stuff like browsing through the feed, liking or commenting. The crawler itself is based on the selenium webdriver library, which can simulate browser interaction.

Since Instagram regularly updates it's site structure, the crawler may not be functional anymore. However, it can give an overview how a bot could work and how selenium can be used.

# Requirements

Selenium webdriver is needed (https://www.selenium.dev/documentation/webdriver/) as an installed library in your local Python. For this project, the webdriver for Chrome was used.

# Structure

This project contains three different parts: Driver.py, InstaFunc.py, InstaStrategy.py

## Driver.py

Think of this as being in the drivers seat for the crawler. It starts and terminates the webbrowser and calls the different functions and/or strategies.

## InstaFunc.py

This script contains all core functionalities.

## InstaStrategy.py

This script is used to bundle different actions together, for example liking and commenting 100 messages.