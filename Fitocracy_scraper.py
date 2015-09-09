# 

import time

from selenium import webdriver
driver = webdriver.PhantomJS()


###################### Preamble: execute once
path_to_chromedriver ='/Users/Lin/Downloads/chromedriver'

#driver = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.fitocracy.com/'
driver.set_window_size(1024,768) #if you don't do this, the window size is too small to find the elements
driver.get(url)

login_xpath = '/html/body/div[2]/div/div/div[2]/a'
driver.find_element_by_xpath(login_xpath).click()


time.sleep(5)


username = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[1]/input')
time.sleep(2)
username.send_keys("XXXXXXXXXX")
password = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[2]/input')
time.sleep(2)
password.send_keys('XXXXXXXXXX')
driver.find_element_by_xpath('//*[@id="login-modal-form"]/button').click()

print "logged in"
time.sleep(30)
driver.set_window_size(1024,768)

todays_points = driver.find_elements_by_xpath("//div/a[contains(text(),'Today')]/preceding-sibling::span")
if todays_points == []:
	print "No points from today"

print "Today's points:" 
print todays_points
total = 0
for today in todays_points:   
    points = today.find_elements_by_class_name("stream_total_points")[0].text
    points = int(points[:-4])
    print points
    total += points
print total

from beeminderpy import Beeminder

my_beeminder = Beeminder('your_auth_token')

my_beeminder.create_datapoint(
	username = 'yourusername',
	goalname = 'yourgoalname',
	timestamp = int(time.time()),
	value = total, 
	comment = 'Scraped from Fitocracy on' + time.ctime())


