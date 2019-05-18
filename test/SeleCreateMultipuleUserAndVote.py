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




class CreateMultipleUserTest(unittest.TestCase):
	def setUp(self):
		executable_path='/usr/local/bin/chromedriver'
		self.driver = webdriver.Chrome(executable_path)

	def test_a_create_user(self):		
		driver = self.driver
		# driver.get(domain + "/login")
		for i in range(1,21):
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
			email.send_keys("test" +str(i)+ "@gmail.com")
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

	def test_b_vote_movie(self):
		driver = self.driver
		for i in range(1,21):
			driver.get("http://0.0.0.0:5000/login")
			self.assertIn("Login", driver.title)
			email=driver.find_element_by_id("email")
			email.clear()
			email.send_keys("test"+str(i)+"@gmail.com")
			password=driver.find_element_by_id("password")
			password.clear()
			password.send_keys("test12345678")
			time.sleep(1)
			driver.find_element_by_id("submit").send_keys(Keys.ENTER)
			driver.get("http://0.0.0.0:5000/polls")
			time.sleep(1)
			driver.find_element_by_id("testMovie").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id(str(random.randint(1,6))).send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_class_name("agree-btn").send_keys(Keys.ENTER)

	def test_b_vote_music(self):
		driver = self.driver
		for i in range(1,21):
			driver.get("http://0.0.0.0:5000/login")
			self.assertIn("Login", driver.title)
			email=driver.find_element_by_id("email")
			email.clear()
			email.send_keys("test"+str(i)+"@gmail.com")
			password=driver.find_element_by_id("password")
			password.clear()
			password.send_keys("test12345678")
			time.sleep(1)
			driver.find_element_by_id("submit").send_keys(Keys.ENTER)
			driver.get("http://0.0.0.0:5000/polls")
			time.sleep(1)
			driver.find_element_by_id("next").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id("testMusic").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id(str(random.randint(7,12))).send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_class_name("agree-btn").send_keys(Keys.ENTER)

	def test_b_vote_recipe(self):
		driver = self.driver
		for i in range(1,21):
			driver.get("http://0.0.0.0:5000/login")
			self.assertIn("Login", driver.title)
			email=driver.find_element_by_id("email")
			email.clear()
			email.send_keys("test"+str(i)+"@gmail.com")
			password=driver.find_element_by_id("password")
			password.clear()
			password.send_keys("test12345678")
			time.sleep(1)
			driver.find_element_by_id("submit").send_keys(Keys.ENTER)
			driver.get("http://0.0.0.0:5000/polls")
			time.sleep(1)
			driver.find_element_by_id("next").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id("next").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id("testRecipe").send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_id(str(random.randint(13,15))).send_keys(Keys.ENTER)
			time.sleep(1)
			driver.find_element_by_class_name("agree-btn").send_keys(Keys.ENTER)
			time.sleep(1)

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()


print('test pass with all case, these test are about create multiple user and vote')






