from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project,Module


class LoginTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """ 初始化数据"""
        User.objects.create_user("test", "test@mail.com", "test123456")
        Project.objects.create(name="testplatform", desc="describition")

    def test_login(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("")
        sleep(4)
        self.driver.find_element_by_id("Loginbutton").click()
        error_hint = self.driver.find_element_by_id("error").text
        self.assertEqual("用户名或密码为空", error_hint)

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("username")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("password")
        sleep(4)
        self.driver.find_element_by_id("Loginbutton").click()
        error_hint = self.driver.find_element_by_id("error").text
        self.assertEqual("用户名或密码错误", error_hint)

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("test")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("test123456")
        sleep(4)
        self.driver.find_element_by_id("Loginbutton").click()
        page_name = self.driver.find_element_by_class_name("navbar-brand").text
        self.assertEqual("测试平台", page_name)

    def test_project_add(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("test")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("test123456")
        self.driver.find_element_by_id("Loginbutton").click()
        sleep(2)
        self.driver.find_element_by_id("add_project").click()
        sleep(1)
        self.driver.find_element_by_id("id_name").send_keys("test project add")
        self.driver.find_element_by_id("id_desc").send_keys("test project add description")
        self.driver.find_element_by_id("add_submit").click()
        sleep(5)
        project_names = self.driver.find_elements_by_id("project_name")
        print(project_names)









