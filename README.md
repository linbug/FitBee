# FitBee

Scrape your day's points from Fitocracy and add them to your Beeminder goal

##Usage
Running this script will pull all of today’s points from Fitocracy and log them to whichever Beeminder goal you like. 

**Note: Your points will be logged each time you run this script, so only run it once at the end of the day!**

The comment “Scraped from Fitocracy on” plus the current timestamp will be sent to Beeminder. Emails are by default set to false.

I’m working on making the browser window headless.


##Configuration

Fill in your Fitocracy and Beeminder usernames and passwords in FitBee.py. 
Get your Beeminder auth token by signing into Beeminder, and then visiting https://www.beeminder.com/api/v1/auth_token.json. 

Download the latest version of the [chromedriver](http://chromedriver.storage.googleapis.com/index.html), unzip it, and set `path_to_chromedriver` as the path to this file.

##Dependencies

1. You will need to install the following Python modules: 
- [time](https://docs.python.org/2/library/time.html) 
- [selenium](https://pypi.python.org/pypi/selenium)
both are installed using `pip`.

2. Clone the [beeminderpy.py](https://github.com/mattjoyce/beeminderpy/blob/master/beeminderpy.py) file and put it in the same directory as FitBee.py. 



