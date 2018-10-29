from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.


class ProjectTest(TestCase):
    """ 项目管理测试"""
    def setUp(self):
        """ 初始化用户，数据及登录操作"""
        User.objects.create_user("admin", "admin@mail.com", "admin123")
        self.client = Client()
        self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})

    def test_project_manage(self):
        """ 项目管理列表页测试"""
        response = self.client.get('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("退出", project_html,)



