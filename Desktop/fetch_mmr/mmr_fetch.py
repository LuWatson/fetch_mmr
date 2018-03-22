import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Chrome('/Users/pxteam/Desktop/fetch_mmr/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.manheim.com/members/powersearch/searchSubmit.do');

#login function
logindata = json.load(open('/Users/pxteam/Desktop/fetch_mmr/login_credentials.json'))
username = driver.find_element_by_id("user_username").send_keys(logindata["username"])
element = driver.find_element_by_id("user_password").send_keys(logindata["password"])
element = driver.find_element_by_name("submit").click()
time.sleep(1)# waits for login to load

##allows user to pass through vin and mileage to get an mmr number
def get_mmr(vin, mileage):
	driver.get('https://mmr.manheim.com/?WT.svl=m_hdr_mnav_buy_mmr&country=US&popup=true&source=man')
	vin=vin
	mileage=mileage
	enter_vin=driver.find_element_by_xpath('//*[@id="vinText"]').send_keys(vin)
	search=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div/form/div/button').click()
	time.sleep(2)
	try:
		mileage=driver.find_element_by_xpath('//*[@id="Odometer"]').send_keys(mileage)
		select_mileage=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/form/div/div[1]/div/div[1]/button').click()
		time.sleep(2)
		mmr=driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div')
		mmr_value=mmr.text
		print (mmr_value)
		return mmr_value
	except:
		print("fetching error")
		return("error")
		pass
	time.sleep(1)
		

