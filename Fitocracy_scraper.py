# 



from selenium import webdriver
#driver = webdriver.PhantomJS()


###################### Preamble: execute once
path_to_chromedriver ='/Users/Lin/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'https://www.fitocracy.com/'
driver.set_window_size(1024,768) #if you don't do this, the window size is too small to find the elements
driver.get(url)

login_xpath = '/html/body/div[2]/div/div/div[2]/a'
driver.find_element_by_xpath(login_xpath).click()

username = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[1]/input')



username = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[1]/input')
username.send_keys("xxxxxxxx")
password = driver.find_element_by_xpath('//*[@id="login-modal-form"]/div[2]/div[2]/input')
password.send_keys('xxxxxxxx')
driver.find_element_by_xpath('//*[@id="login-modal-form"]/button').click()

todays_points = driver.find_elements_by_xpath("//div/a[contains(text(),'Today')]/preceding-sibling::span")

total = 0
for today in todays_points:   
    points = today.find_elements_by_class_name("stream_total_points")[0].text
    points = int(points[:-4])
    total += points
total