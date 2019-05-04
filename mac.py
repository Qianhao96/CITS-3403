from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/local/bin/chromedriver')
driver.get('https://www.google.co.in')