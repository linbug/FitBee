#!/usr/bin/env python
##################### Fill out your details
Fitocracy_username 	= 'linbug'
Fitocracy_password 	= 'QmrXK8A9ALP'
Beeminder_authtoken = '45kTWEpaE622FYivqpGE' 
Beeminder_username	= 'jeffalstott'
Beeminder_goalname	= 'workout'
path_to_chromedriver 		='/Users/Lin/Downloads/chromedriver'

##################### Import dependencies

import time
from selenium import webdriver
from beeminderpy import Beeminder
#from pyvirtualdisplay import Display
#driver = webdriver.PhantomJS()

###################### Open up Fitocracy in your browser

#display = Display(visible=0, size=(800, 600))
#display.start()
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'https://www.fitocracy.com/'
driver.set_window_size(1024,768) #if you don't do this, the window size is too small to find the elements
driver.get(url)
time.sleep(5)

###################### Define functions

def login_to_Fitocracy():
	print("Logging into Fitocracy...")
	login_xpath = '/html/body/div[2]/div/div/div[2]/a'
	driver.find_element_by_xpath(login_xpath).click()
	time.sleep(2)
	username = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[1]/input')
	time.sleep(2)
	username.send_keys(Fitocracy_username)
	password = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[2]/input')
	time.sleep(3)
	password.send_keys(Fitocracy_password)
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="login-modal-form"]/button').click()

def check_if_login_worked():
	time.sleep(5)
	if driver.current_url == 'https://www.fitocracy.com/home/':
		return(1)
	else:
		return(0)

def scrape_todays_points():
	print("Scraping points")
	time.sleep(10)
	todays_points = driver.find_elements_by_xpath("//div/a[contains(text(),'Today')]/preceding-sibling::span")
	total = 0
	for today in todays_points:   
	    points = today.find_elements_by_class_name("stream_total_points")[0].text
	    points = int(points[:-4].replace(',', ''))
	    total += points
	driver.close()
	if todays_points == []:
		print("No points from today (maybe something went wrong?) :C")
	else:
		print("Today you earned " + str(total) + " points!")
	return total

def send_points_to_Beeminder(total):

	print("Sending points to Beeminder")
	my_beeminder = Beeminder(Beeminder_authtoken)
	my_beeminder.create_datapoint(
		username = Beeminder_username,
		goalname = Beeminder_goalname,
		timestamp = int(time.time()),
		value = total, 
		comment = 'Scraped from Fitocracy on ' + time.ctime())

####################### Execute functions
driver.set_window_size(1024,768)
login_to_Fitocracy()
check = check_if_login_worked()
if check:
	print("Login successful")
	driver.set_window_size(1024,768)
	total_points = scrape_todays_points()
	send_points_to_Beeminder(total_points)
else:
	print("Login failed") 

#display.stop()
