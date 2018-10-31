from django.test import TestCase,Client
from django.contrib.auth.models import User
from project_app.models import Project, Module

# Create your tests here.


class ProjectPageTest(TestCase):
    """ 项目管理页面测试"""
    def setUp(self):
        """ 初始化用户，数据及登录操作"""
        User.objects.create_user("admin", "admin@mail.com", "admin123")
        Project.objects.create(name="project test", desc="project test describe")
        self.client = Client()
        self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})

    def test_project_manage_page(self):
        """ 项目管理列表页测试"""
        response = self.client.get('/manage/project_manage/')
        project_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("退出", project_html)
        self.assertIn("project test", project_html)

    def test_project_add_page(self):
        """ 增加项目列表页测试"""
        response = self.client.get('/manage/add_project/')
        self.assertEqual(response.status_code, 200)

    def test_project_edit_page(self):
        """ 编辑项目列表页测试"""
        Project.objects.create(name="project test edit", desc="project test edit describe")
        project = Project.objects.get(name="project test edit")
        response = self.client.get('/manage/edit_project/' + str(project.id) + "/")
        project_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("project test edit", project_html)

    def test_project_delete_page(self):
        """ 删除项目列表页测试"""
        Project.objects.create(name="project test delete", desc="project test delete describe")
        project = Project.objects.get(name="project test delete")
        response = self.client.get('/manage/del_project/' + str(project.id) + "/")
        self.assertEqual(response.status_code, 302)


class ProjectTest(TestCase):
    """ 项目管理测试"""
    def setUp(self):
        """ 初始化用户，数据及登录操作"""
        User.objects.create_user("admin", "admin@mail.com", "admin123")
        Project.objects.create(name="project test", desc="project test describe")
        self.client = Client()
        self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})

    def test_project_add(self):
        """ 项目添加测试"""
        data = {"name": "project add test", "desc": "project add test describe", "status": True}
        response = self.client.post('/manage/add_project/',data=data)
        self.assertEqual(response.status_code, 302)

    def test_project_edit(self):
        """ 编辑项目测试"""
        Project.objects.create(name="project test edit", desc="project test edit describe")
        project = Project.objects.get(name="project test edit")
        data = {"name": "project test edit edit", "desc": "project test edit edit describe", "status": True}
        response = self.client.post('/manage/edit_project/' + str(project.id) + '/', data=data)
        self.assertEqual(response.status_code, 302)

    def test_project_delete(self):
        """ 删除项目测试"""
        Project.objects.create(name="project test delete", desc="project test delete describe")
        project = Project.objects.get(name="project test delete")
        response = self.client.post('/manage/del_project/' + str(project.id) + '/')
        self.assertEqual(response.status_code, 302)


class ModuleTest(TestCase):
    """ 模块管理测试"""
    def setUp(self):
        """ 初始化用户，数据及登录操作"""
        User.objects.create_user("admin", "admin@mail.com", "admin123")
        Project.objects.create(name="project test", desc="project test describe")
        self.client = Client()
        self.client.post('/login_action/', data={'username': 'admin', 'password': 'admin123'})

    def test_module_add(self):
        """ 模块增加测试"""
        data={"name": "module add test", "desc": "module add test describe", "project_name": "project test", "status": True}
        response = self.client.post('/manage/add_module/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_module_edit(self):
        """ 编辑模块测试"""
        project = Project.objects.get(name="project test")
        Module.objects.create(name="module test edit", desc="module test edit describe", project_name=project)
        module = Module.objects.get(name="module test edit")
        data = {"name": "module test edit edit", "desc": "module test edit edit describe",
                "project_name": project}
        response = self.client.post('/manage/edit_module/' + str(module.id) + '/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_module_delete(self):
        """ 删除模块测试"""
        project = Project.objects.get(name="project test")
        Module.objects.create(name="module test delete", desc="module test delete describe", project_name=project)
        module = Module.objects.get(name="module test delete")
        response = self.client.post('/manage/del_module/' + str(module.id) + '/')
        self.assertEqual(response.status_code, 302)





