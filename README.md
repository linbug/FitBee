# FitBee

Scrape your day's points from Fitocracy and add them to your Beeminder goal

##Usage
Running this script will pull all of today’s points from Fitocracy and log them to whichever Beeminder goal you like. 

Should work with both Python 2 and Python 3.

**Note: Your points will be logged each time you run this script, so only run it once at the end of the day!**
**Also note: this will not work if you are following other people, since it takes any points logged today from your news stream. (I can modify this on request)**

The comment “Scraped from Fitocracy on” plus the current timestamp will be sent to Beeminder. Emails are by default set to false.

I’m working on making the browser window headless. 

##Dependencies

1. You will need to install the following Python module: 
	- [selenium](https://pypi.python.org/pypi/selenium)
	
	using `pip`.

2. Clone the [beeminderpy.py](https://github.com/jeffalstott/beeminderpy/blob/545c742db394d23d496aa1d1bef65959ec47a1cb/beeminderpy.py) file and put it in the same directory as FitBee.py. 

3. Download the latest version of the [chromedriver](http://chromedriver.storage.googleapis.com/index.html), unzip it, and note the path to this file

##Configuration

- Fill in your Fitocracy and Beeminder usernames and passwords in FitBee.py. 
Get your Beeminder auth token by signing into Beeminder, and then visiting: https://www.beeminder.com/api/v1/auth_token.json. 

- set `path_to_chromedriver` as the path to where you downloaded chromedriver

 



