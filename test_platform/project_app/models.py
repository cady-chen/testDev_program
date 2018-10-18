from django.db import models

# Create your models here.
#项目表  class = table; 变量 = 表中的字段
#下面创建项目表，表名为:user_app_ProjectInfo
#django提供的字段类型查看在：D:\Program Files\Python\Python36-32\Lib\site-packages\django\db\models\fields目录下的__init__.py文件里
#blank字段的值是针对于页面上的表单来说，blank=True表示表单对应的字段可为空，blank=False表示表单对应的字段不可为空；
#null针对的是数据库，null=True表明数据库里该字段可为空，null=False表明数据库里该字段不可为空
class Project(models.Model):
    name = models.CharField("项目名称", blank=False,max_length=1000)
    desc = models.CharField("项目描述",blank=True, max_length=5000)
    status = models.BooleanField("项目状态", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


#模块表
class Module(models.Model):
    name = models.CharField("模块名称", blank=False, max_length=1000)
    desc = models.CharField("模块描述", blank=True, max_length=5000)
    project_name = models.ForeignKey(Project, blank=False, null=False, on_delete=models.CASCADE)
    create_time = models.DateTimeField("创建时间", auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

