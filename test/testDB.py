from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
from flask_bcrypt import Bcrypt
from survey import create_app
app = create_app()
app.app_context().push()
from survey.models import db

class Database(unittest.TestCase):

    def setUp(self):
        executable_path='/usr/local/bin/chromedriver'
        self.driver = webdriver.Chrome(executable_path)
        db.create_all()

    def test_creat_admin(self):
        from survey.models import User
        bcrypt = Bcrypt()
        hashed_pw=bcrypt.generate_password_hash('test12345678').decode('utf-8')
        user=User(firstname='Qianhao', lastname='Liu',email='qianhao.liu@gmail.com', password=hashed_pw, gender='M', is_admin=True)
        db.session.add(user)
        db.session.commit()


    def tearDown(self):
        driver = self.driver
        # driver.get(domain + "/login")
        driver.get("http://0.0.0.0:5000/login")
        email=driver.find_element_by_id("email")
        email.clear()
        email.send_keys("qianhao.liu@gmail.com")
        password=driver.find_element_by_id("password")
        password.clear()
        password.send_keys("test12345678")
        time.sleep(1)
        driver.find_element_by_id("submit").send_keys(Keys.ENTER)
        assert "Login successfull" in driver.page_source

if __name__ == "__main__":
    unittest.main()