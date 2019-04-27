from survey import create_app
import unittest
# import pytest
app = create_app()



class FlaskTestCase(unittest.TestCase):

	# # make sure home page can be accessed
	# def test_index(self):
	# 	tester = app.test_client(self)
	# 	response = tester.get('/', content_type='html/text')
	# 	self.assertEqual(response.status_code, 200)


	# make sure login page can be loaded 
	def test_login_page_load(self):
		tester = app.test_client(self)
		response = tester.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# make sure login behavier is correct given a correct credential
	def test_login_with_corrent_credential(self):
		tester = app.test_client(self)
		response = tester.post(
			'/admin/',
			 data=dict(email="admin@gmail.com",
			 		   password="admin"),
			 		   follow_redirects=True)
		self.assertIn(b'Login successfull', response.data)
		# self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
	unittest.main()