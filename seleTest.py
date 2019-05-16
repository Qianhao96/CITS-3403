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

# This part test all functionality for use admin

# class AdminTest(unittest.TestCase):

# 	def setUp(self):
# 		executable_path='/usr/local/bin/chromedriver'
# 		self.driver = webdriver.Chrome(executable_path)

# 	def test_a_admin_add_and_delete_user(self):
# 		driver = self.driver
# 		# driver.get(domain + "/login")
# 		driver.get("http://0.0.0.0:5000/login")
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("qianhao.liu@gmail.com")
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		assert "Login successfull" in driver.page_source
# 		driver.get("http://0.0.0.0:5000/user_admin")
# 		add_user=driver.find_element_by_id("qianhao.liu@gmail.comadd")
# 		add_user.send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		firstname=driver.find_element_by_id("firstname")
# 		firstname.clear()
# 		firstname.send_keys("test")
# 		lastname=driver.find_element_by_id("lastname")
# 		lastname.clear()
# 		lastname.send_keys("test")
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("admintest@gmail.com")
# 		gender=driver.find_element_by_id("gender-0")
# 		gender.send_keys(Keys.SPACE)
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		confirm_password=driver.find_element_by_id("confirm_password")
# 		confirm_password.clear()
# 		confirm_password.send_keys("test12345678")
# 		time.sleep(1)
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		assert "New user account has been created!" in driver.page_source
# 		delete_user=driver.find_element_by_id("admintest@gmail.comdelete")
# 		delete_user.send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		admin_delete_user=driver.find_element_by_id("admin_delete_user")
# 		admin_delete_user.send_keys(Keys.ENTER)
# 		driver.refresh()
# 		assert "admintest@gmail.com" not in driver.page_source

# 	def test_b_admin_add_and_delete_poll(self):
# 		driver = self.driver
# 		# driver.get(domain + "/login")
# 		driver.get("http://0.0.0.0:5000/login")
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("qianhao.liu@gmail.com")
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		assert "Login successfull" in driver.page_source
# 		driver.get("http://0.0.0.0:5000/user_admin")
# 		driver.find_element_by_id("v-pills-poll-tab").send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		driver.find_element_by_id("poll_add").send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		poll_name=driver.find_element_by_id("poll_name")
# 		poll_name.send_keys('Avenger')
# 		video=driver.find_element_by_id("video")
# 		video.send_keys('https://www.youtube.com/embed/TcMBFSGVi1c')
# 		poll_description=driver.find_element_by_id("description")
# 		poll_description.send_keys('Avenger')
# 		time.sleep(1)
# 		driver.find_element_by_id("poll_submit").send_keys(Keys.ENTER)
# 		driver.refresh()
# 		assert "Avenger" in driver.page_source
# 		driver.find_element_by_id("v-pills-poll-tab").send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		driver.find_element_by_id("pollAvengerdelete").send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		driver.find_element_by_id("admin_delete_poll").send_keys(Keys.ENTER)


# 	def tearDown(self):
# 		self.driver.close()

# # This part test login and logout with a correct credential

# class LoginLogoutRegisterTest(unittest.TestCase):
# 	def setUp(self):
# 		executable_path='/usr/local/bin/chromedriver'
# 		self.driver = webdriver.Chrome(executable_path)

# 	def test_d_register(self):		
# 		driver = self.driver
# 		# driver.get(domain + "/login")
# 		driver.get("http://0.0.0.0:5000/register")
# 		self.assertIn("Register", driver.title)
# 		firstname=driver.find_element_by_id("firstname")
# 		firstname.clear()
# 		firstname.send_keys("test")
# 		lastname=driver.find_element_by_id("lastname")
# 		lastname.clear()
# 		lastname.send_keys("test")
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("test@gmail.com")
# 		gender=driver.find_element_by_id("gender-0")
# 		gender.send_keys(Keys.SPACE)
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		confirm_password=driver.find_element_by_id("confirm_password")
# 		confirm_password.clear()
# 		confirm_password.send_keys("test12345678")
# 		time.sleep(1)
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		time.sleep(1)
# 		assert "Your account has been created! You are now able to login" in driver.page_source

# 	def test_e_login_logout_with_correct_and_incorrect_credential(self):
# 		driver = self.driver
# 		# driver.get(domain + "/login")
# 		driver.get("http://0.0.0.0:5000/login")
# 		self.assertIn("Login", driver.title)
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("test1111111@gmail.com")
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		assert "Login unsuccessful. Please check Email and Password" in driver.page_source
# 		email=driver.find_element_by_id("email")
# 		email.clear()
# 		email.send_keys("test@gmail.com")
# 		password=driver.find_element_by_id("password")
# 		password.clear()
# 		password.send_keys("test12345678")
# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
# 		assert "Login successfull" in driver.page_source
# 		driver.find_element_by_id("logout").send_keys(Keys.ENTER)
# 		assert "Logout successfull" in driver.page_source


# 	def tearDown(self):
# 		self.driver.close()


class LoginLogoutRegisterTest(unittest.TestCase):
	def setUp(self):
		executable_path='/usr/local/bin/chromedriver'
		self.driver = webdriver.Chrome(executable_path)

	# def test_f_create_user(self):		
	# 	driver = self.driver
	# 	# driver.get(domain + "/login")
	# 	for i in range(1,21):
	# 		driver.get("http://0.0.0.0:5000/register")
	# 		self.assertIn("Register", driver.title)
	# 		firstname=driver.find_element_by_id("firstname")
	# 		firstname.clear()
	# 		firstname.send_keys("test")
	# 		lastname=driver.find_element_by_id("lastname")
	# 		lastname.clear()
	# 		lastname.send_keys("test")
	# 		email=driver.find_element_by_id("email")
	# 		email.clear()
	# 		email.send_keys("test" +str(i)+ "@gmail.com")
	# 		gender=driver.find_element_by_id("gender-0")
	# 		gender.send_keys(Keys.SPACE)
	# 		password=driver.find_element_by_id("password")
	# 		password.clear()
	# 		password.send_keys("test12345678")
	# 		confirm_password=driver.find_element_by_id("confirm_password")
	# 		confirm_password.clear()
	# 		confirm_password.send_keys("test12345678")
	# 		time.sleep(1)
	# 		driver.find_element_by_id("submit").send_keys(Keys.ENTER)
	# 		time.sleep(1)
	# 		assert "Your account has been created! You are now able to login" in driver.page_source

	def test_f_vote(self):
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


# print('test pass with all case')






