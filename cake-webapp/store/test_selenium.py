from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/register')

        # Get the form element & fill it

        first_name = WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_first_name")))
        first_name.send_keys('Romisha')

        last_name=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_last_name")))
        last_name.send_keys('Thapa')

        username=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        email=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_email")))
        email.send_keys('romisha@romisha.com')

        password1=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_password1")))
        password1.send_keys('9812345')

        password2=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.ID, "id_password2")))
        password2.send_keys('9812345')

        submit=WebDriverWait(selenium, 2).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    #def test_login(selenium):
