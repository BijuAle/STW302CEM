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

        first_name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_first_name")))
        first_name.send_keys('Romisha')

        last_name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_last_name")))
        last_name.send_keys('Thapa')

        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        email = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_email")))
        email.send_keys('romisha@romisha.com')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password1")))
        password1.send_keys('9812345')

        password2 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password2")))
        password2.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_login(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_product_list(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/list')

        # check the returned result
        assert '' in selenium.page_source

    def test_product(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/list')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "img-rounded")))
        product.click()

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/products/1/')

        # check the returned result
        assert '' in selenium.page_source

    def test_add_to_cart(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/list')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "img-rounded")))
        product.click()

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/products/1/')

        add = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "badge")))
        add.click()

        # check the returned result
        assert '' in selenium.page_source

    def test_remove_from_cart(self):
        selenium = self.selenium

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('romisha')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('9812345')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/list')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "img-rounded")))
        product.click()

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/products/1/')

        remove = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, "badge")))
        remove.click()

        # check the returned result
        assert '' in selenium.page_source

# 'Admin Login, Product UD, Cart View, Admin change PWD, Admin logout '


class AdminTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(
            'C:/Users/User/Desktop/STW302CEM/chromedriver.exe')
        super(AdminTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AdminTestCase, self).tearDown()

    def test_admin_login(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_product_add(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addproduct = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,
             "//a[@href='/admin/store/product/add/']")))
        addproduct.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/product/add/')

        name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_name")))
        name.send_keys('sweet cake')

        description = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_description")))
        description.send_keys('sweet cake descriptionsssss')

        occasion = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='occasion']")))
        occasion.send_keys(Keys.RETURN)

        price = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_price")))
        price.send_keys('2100')

        discount = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_discount_rate")))
        discount.send_keys('60')

        SaleStartDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_0")))
        SaleStartDate.send_keys('2019-11-01')

        SaleStartTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_1")))
        SaleStartTime.send_keys('06:00:00')

        SaleEndDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_0")))
        SaleEndDate.send_keys('2019-11-06')

        SaleEndTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_1")))
        SaleEndTime.send_keys('08:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)
        # check the returned result
        assert '' in selenium.page_source

    def test_admin_product_update(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addproduct = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,
             "//a[@href='/admin/store/product/add/']")))
        addproduct.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/product/add/')

        name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_name")))
        name.send_keys('sweet cake')

        description = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_description")))
        description.send_keys('sweet cake descriptionsssss')

        occasion = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='occasion']")))
        occasion.send_keys(Keys.RETURN)

        price = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_price")))
        price.send_keys('2100')

        discount = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_discount_rate")))
        discount.send_keys('60')

        SaleStartDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_0")))
        SaleStartDate.send_keys('2019-11-01')

        SaleStartTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_1")))
        SaleStartTime.send_keys('06:00:00')

        SaleEndDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_0")))
        SaleEndDate.send_keys('2019-11-06')

        SaleEndTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_1")))
        SaleEndTime.send_keys('08:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/product/')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,"//a[@href='/admin/store/product/27/change/']")))
        product.send_keys(Keys.RETURN)

        name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_name")))
        name.send_keys('sour cake')

        description = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_description")))
        description.send_keys('sour cake descriptionsssss')

        occasion = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='occasion']")))
        occasion.send_keys(Keys.RETURN)

        price = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_price")))
        price.send_keys('2000')

        discount = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_discount_rate")))
        discount.send_keys('70')

        SaleStartDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_0")))
        SaleStartDate.send_keys('2019-12-01')

        SaleStartTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_1")))
        SaleStartTime.send_keys('07:00:00')

        SaleEndDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_0")))
        SaleEndDate.send_keys('2019-12-06')

        SaleEndTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_1")))
        SaleEndTime.send_keys('09:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_product_delete(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addproduct = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/store/product/add/']")))
        addproduct.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/product/add/')

        name = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_name")))
        name.send_keys('sweet cake')

        description = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_description")))
        description.send_keys('sweet cake descriptionsssss')

        occasion = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='occasion']")))
        occasion.send_keys(Keys.RETURN)

        price = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_price")))
        price.send_keys('2100')

        discount = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_discount_rate")))
        discount.send_keys('60')

        SaleStartDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_0")))
        SaleStartDate.send_keys('2019-11-01')

        SaleStartTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_start_1")))
        SaleStartTime.send_keys('06:00:00')

        SaleEndDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_0")))
        SaleEndDate.send_keys('2019-11-06')

        SaleEndTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_sale_end_1")))
        SaleEndTime.send_keys('08:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/product/')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/store/product/28/change/']")))
        product.send_keys(Keys.RETURN)

        delete = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/store/product/28/delete/']")))
        delete.send_keys(Keys.RETURN)

        sure = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        sure.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_cart_add(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addcarts = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,
             "//a[@href='/admin/store/cart/add/']")))
        addcarts.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/add/')

        user = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_user")))
        user.send_keys('sushan')

        items = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='items']")))
        items.send_keys(Keys.RETURN)

        OrderedDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_0")))
        SaleStartDate.send_keys('2019-11-01')

        OrderedTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_1")))
        SaleStartTime.send_keys('06:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)
        # check the returned result
        assert '' in selenium.page_source

    def test_admin_carts_update(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addcarts = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,
             "//a[@href='/admin/store/cart/add/']")))
        addcarts.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/add/')

        user = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_user")))
        user.send_keys('sushan')

        items = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='items']")))
        items.send_keys(Keys.RETURN)

        OrderedDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_0")))
        SaleStartDate.send_keys('2019-11-01')

        OrderedTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_1")))
        SaleStartTime.send_keys('06:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/')

        carts = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,"//a[@href='/admin/store/cart/6/change/']")))
        carts.send_keys(Keys.RETURN)

        user = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_user")))
        user.send_keys('sushan')

        items = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='items']")))
        items.send_keys(Keys.RETURN)

        OrderedDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_0")))
        SaleStartDate.send_keys('2019-11-01')

        OrderedTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_1")))
        SaleStartTime.send_keys('06:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_carts_delete(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        addcarts = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,
             "//a[@href='/admin/store/cart/add/']")))
        addcarts.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/add/')

        user = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_user")))
        user.send_keys('sushan')

        items = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='items']")))
        items.send_keys(Keys.RETURN)

        OrderedDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_0")))
        SaleStartDate.send_keys('2019-11-01')

        OrderedTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_1")))
        SaleStartTime.send_keys('06:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/')

        carts = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH,"//a[@href='/admin/store/cart/6/change/']")))
        carts.send_keys(Keys.RETURN)

        user = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_user")))
        user.send_keys('sushan')

        items = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='items']")))
        items.send_keys(Keys.RETURN)

        OrderedDate = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_0")))
        SaleStartDate.send_keys('2019-11-01')

        OrderedTime = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_ordered_date_1")))
        SaleStartTime.send_keys('06:00:00')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='_save']")))
        submit.send_keys(Keys.RETURN)

        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin/store/cart/')

        product = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/store/cart/6/change/']")))
        product.send_keys(Keys.RETURN)

        delete = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/store/cart/6/delete/']")))
        delete.send_keys(Keys.RETURN)

        sure = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
        sure.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_change_password(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        ChangePassword = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/password_change/']")))
        ChangePassword.send_keys(Keys.RETURN)

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_old_password")))
        password1.send_keys('biju')

        password2 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_new_password1")))
        password2.send_keys('biju')

        password3 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_new_password2")))
        password3.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Change my password']")))
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source

    def test_admin_logout(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/admin')

        # Get the form element & fill it
        username = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_username")))
        username.send_keys('biju')

        password1 = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password1.send_keys('biju')

        submit = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='Log in']")))
        submit.send_keys(Keys.RETURN)

        logout = WebDriverWait(selenium, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/admin/logout/']")))
        logout.send_keys(Keys.RETURN)

        # check the returned result
        assert '' in selenium.page_source
