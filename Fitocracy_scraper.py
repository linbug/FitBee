##################### Fill out your details
Fitocracy_username 	= 'your_Fitocracy_username'
Fitocracy_password 	= 'your_Fitocracy_password'
Beeminder_authtoken = 'your_Beeminder_auth_token' #get your auth token by signing into Beeminder, and then visiting https://www.beeminder.com/api/v1/auth_token.json
Beeminder_username	= 'your_Beeminder_username'
Beeminder_password	= 'your_Beeminder_password'

##################### Import dependencies

import time
from selenium import webdriver
path_to_chromedriver ='/Users/Lin/Downloads/chromedriver'
from beeminderpy import Beeminder

#driver = webdriver.PhantomJS()

###################### Open up Fitocracy in your browser

#driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.fitocracy.com/'
driver.set_window_size(1024,768) #if you don't do this, the window size is too small to find the elements
driver.get(url)

###################### Define functions

def login_to_Fitocracy():
	print "Logging into Fitocracy..."
	login_xpath = '/html/body/div[2]/div/div/div[2]/a'
	driver.find_element_by_xpath(login_xpath).click()
	time.sleep(5)
	username = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[1]/input')
	time.sleep(2)
	username.send_keys(Fitocracy_username)
	password = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[2]/input')
	time.sleep(2)
	password.send_keys(Fitocracy_password)
	driver.find_element_by_xpath('//*[@id="login-modal-form"]/button').click()
	print "Logged in"

# time.sleep(30)
# driver.set_window_size(1024,768)

def scrape_todays_points():
	print "Scraping points"
	todays_points = driver.find_elements_by_xpath("//div/a[contains(text(),'Today')]/preceding-sibling::span")
	if todays_points == []:
	print "No points from today"
	total = 0
	for today in todays_points:   
	    points = today.find_elements_by_class_name("stream_total_points")[0].text
	    points = int(points[:-4])
	    print points
	    total += points
	return total

def send_points_to_Beeminder(total):
	print "Sending points to Beeminder"
	my_beeminder = Beeminder(Beeminder_authtoken)
	my_beeminder.create_datapoint(
		username = Beeminder_username,
		goalname = Beeminder_password,
		timestamp = int(time.time()),
		value = total, 
		comment = 'Scraped from Fitocracy on' + time.ctime())

####################### Execute functions

login_to_Fitocracy()
total_points = scrape_todays_points()
send_points_to_Beeminder(total_points)


