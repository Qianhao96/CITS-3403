from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
import random


# print("Please enter the path for 'chromedriver', Normally this should be stored in /usr/local/bin/chromedriver(For mac)")
# executable_path=input()
# print('Please enter the domain for this app, either localhost or https://ycj-lqh-master.herokuapp.com')
# domain = input()
# executable_path='/usr/local/bin/chromedriver'
# driver = webdriver.Chrome(executable_path)


# This part test login and logout with a correct credential

class LoginLogoutRegisterTest(unittest.TestCase):
	def setUp(self):
		executable_path='/usr/local/bin/chromedriver'
		self.driver = webdriver.Chrome(executable_path)

	def test_d_register(self):		
		driver = self.driver
		# driver.get(domain + "/login")
		driver.get("http://0.0.0.0:5000/register")
		self.assertIn("Register", driver.title)
		firstname=driver.find_element_by_id("firstname")
		firstname.clear()
		firstname.send_keys("test")
		lastname=driver.find_element_by_id("lastname")
		lastname.clear()
		lastname.send_keys("test")
		email=driver.find_element_by_id("email")
		email.clear()
		email.send_keys("test@gmail.com")
		gender=driver.find_element_by_id("gender-0")
		gender.send_keys(Keys.SPACE)
		password=driver.find_element_by_id("password")
		password.clear()
		password.send_keys("test12345678")
		confirm_password=driver.find_element_by_id("confirm_password")
		confirm_password.clear()
		confirm_password.send_keys("test12345678")
		time.sleep(1)
		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
		time.sleep(1)
		assert "Your account has been created! You are now able to login" in driver.page_source

	def test_e_login_logout_with_correct_and_incorrect_credential(self):
		driver = self.driver
		# driver.get(domain + "/login")
		driver.get("http://0.0.0.0:5000/login")
		self.assertIn("Login", driver.title)
		email=driver.find_element_by_id("email")
		email.clear()
		email.send_keys("test1111111@gmail.com")
		password=driver.find_element_by_id("password")
		password.clear()
		password.send_keys("test12345678")
		time.sleep(1)
		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
		assert "Login unsuccessful. Please check Email and Password" in driver.page_source
		email=driver.find_element_by_id("email")
		email.clear()
		email.send_keys("test@gmail.com")
		password=driver.find_element_by_id("password")
		password.clear()
		password.send_keys("test12345678")
		time.sleep(1)
		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
		assert "Login successfull" in driver.page_source
		driver.find_element_by_id("logout").send_keys(Keys.ENTER)
		assert "Logout successfull" in driver.page_source


	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()


print('test pass with all case, these test are about create user and login with incrooect credential and then with acorrect credential')