from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
# django 的单元测试


class UserModelsTest(TestCase):

    def setUp(self):
        """
        创建数据
        """
        User.objects.create_user("test01", "test01@mail.com", "test123456")

    def test_user_query(self):
        """
        测试查询用户用例
        """
        user = User.objects.get(username="test01")
        self.assertEqual(user.email, "test01@mail.com")

    def test_user_create(self):
        """
        测试创建用户用例
        """
        User.objects.create_user("test02","test02@mail.com","test654321")
        user = User.objects.get(username="test02")
        self.assertEqual(user.email, "test02@mail.com")

    def test_user_update(self):
        """
        测试更新用户用例
        """
        user = User.objects.get(username="test01")
        user.username = "test03"
        user.email = "test03@mail.com"
        user.save()
        user2 = User.objects.get(username="test03")
        self.assertEqual(user2.email, 'test03@mail.com')

    def test_user_delete(self):
        """
        测试用户删除用例
        """
        user = User.objects.get(username="test01")
        user.delete()
        user2 = User.objects.all()
        self.assertEqual(len(user2), 0)


class IndexPageTest(TestCase):
    """测试login登录首页"""

    def test_index_page_renders_index_template(self):
        """断言是否用给定的login.html模版响应"""
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')


class LoginActionTest(TestCase):
    """测试登录"""

    def setUp(self):
        """ 数据的初始化"""
        User.objects.create_user("admin", "admin@mail.com","admin123")
        self.client = Client()

    def test_user_add(self):
        """ 测试添加用户用例"""
        user = User.objects.get(username="admin")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@mail.com")

    def test_login_null(self):
        """ 测试用户名密码为空的登录用例"""
        response = self.client.post('/login_action/', data={'username': '', 'password': ''})
        login_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code,200)
        self.assertIn("用户名或密码为空", login_html)

    def test_login_error(self):
        """ 测试用户名密码错误的登录用例"""
        response = self.client.post('/login_action/', data={'username': '1212', 'password': '123456'})
        login_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误", login_html)

    def test_login_success(self):
        """ 登录成功"""
        response = self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})
        self.assertEqual(response.status_code, 302)


class LogoutTest(TestCase):
    """ 测试退出"""

    def setUp(self):
        User.objects.create_user("admin", "admin@mail.com","admin123")
        self.client = Client()
        response = self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})


    def test_logout(self):
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)