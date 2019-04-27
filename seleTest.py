from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

# print('Please enter the path for "chromedriver"')
# executable_path=input()
# print('Please enter the domain for this app, either localhost or https://ycj-lqh-master.herokuapp.com')
# domain = input()
executable_path='../3403/bin/chromedriver'
driver = webdriver.Chrome(executable_path)

# This part test login and logout with a correct credential
def login_logout_with_correct_credential():
	driver.get("http://0.0.0.0:5000/login")
	driver.find_element_by_id("email").send_keys("qianhao.liu1@gmail.com")
	driver.find_element_by_id("password").send_keys("test12345678")
	driver.find_element_by_id("submit").send_keys(Keys.ENTER)
	time.sleep(1)
	driver.find_element_by_id("logout").send_keys(Keys.ENTER)

	time.sleep(2)
	print('test pass with all case')
	driver.quit()


login_logout_with_correct_credential()