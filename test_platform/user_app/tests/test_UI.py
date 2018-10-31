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


class ProjectTests(StaticLiveServerTestCase):

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
        """ 初始化数据及登录"""
        User.objects.create_user("test", "test@mail.com", "test123456")
        Project.objects.create(name="testplatform", desc="describition")
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("test")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("test123456")
        self.driver.find_element_by_id("Loginbutton").click()
        sleep(2)

    def test_project_add(self):
        self.driver.find_element_by_id("add_project").click()
        sleep(1)
        self.driver.find_element_by_id("id_name").send_keys("test project add")
        self.driver.find_element_by_id("id_desc").send_keys("test project add description")
        self.driver.find_element_by_id("add_submit").click()
        sleep(2)
        self.assertIn("test project add", self.driver.page_source) #判断新增的项目是否在当前页面的源码中

    def test_project_edit(self):
        self.driver.find_element_by_xpath("//td/a[contains(text(),'编辑')]").click()
        sleep(1)
        self.driver.find_element_by_id("id_name").clear()
        self.driver.find_element_by_id("id_name").send_keys("testplatform edit")
        self.driver.find_element_by_id("id_desc").clear()
        self.driver.find_element_by_id("id_desc").send_keys("testplatform edit description")
        self.driver.find_element_by_id("edit_submit").click()
        sleep(2)
        self.assertIn("testplatform edit", self.driver.page_source)

    def test_project_delete(self):
        self.driver.find_element_by_xpath("//td/a[contains(text(),'删除')]").click()
        self.assertNotIn("testplatform", self.driver.page_source)


class ModuleTests(StaticLiveServerTestCase):

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
        """ 初始化数据及登录"""
        User.objects.create_user("test", "test@mail.com", "test123456")
        Project.objects.create(name="testplatform", desc="describition")
        Module.objects.create(name="testplatform module1", desc="module1 description",
                              project_name=Project.objects.get(name="testplatform"))
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_id("inputUsername")
        username_input.send_keys("test")
        password_input = self.driver.find_element_by_id("inputPassword")
        password_input.send_keys("test123456")
        self.driver.find_element_by_id("Loginbutton").click()
        sleep(2)
        self.driver.find_element_by_id("module_manage").click()

    def test_module_add(self):
        self.driver.find_element_by_id("add_module").click()
        self.driver.find_element_by_id("id_name").send_keys("test module add")
        self.driver.find_element_by_id("id_desc").send_keys("test module add description")
        self.driver.find_element_by_id("id_project_name").click()
        self.driver.find_element_by_xpath(" // *[ @ id = 'id_project_name'] / option[2]").click()
        self.driver.find_element_by_id("add_module_submit").click()
        sleep(2)
        self.assertIn("test module add", self.driver.page_source)

    def test_module_edit(self):
        self.driver.find_element_by_xpath("//td/a[contains(text(),'编辑')]").click()
        self.driver.find_element_by_id("id_name").clear()
        self.driver.find_element_by_id("id_name").send_keys("testplatform module1 edit")
        self.driver.find_element_by_id("id_desc").clear()
        self.driver.find_element_by_id("id_desc").send_keys("module1 description edit")
        self.driver.find_element_by_id("edit_module_submit").click()
        sleep(2)
        self.assertIn("testplatform module1 edit", self.driver.page_source)

    def test_module_delete(self):
        self.driver.find_element_by_xpath("//td/a[contains(text(),'删除')]").click()
        self.assertNotIn("testplatform module1", self.driver.page_source)



















