from django.db import models
from project_app.models import Project,Module

# Create your models here.
class TestCase(models.Model):
    """
    用例列表
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=1000, blank=False, default="")
    url = models.TextField("URL", default="")
    req_method = models.CharField("请求方法", max_length=10, default="")
    req_type = models.CharField("参数类型",max_length=10, default="")
    req_header = models.TextField("header",default="")
    req_parameter = models.TextField("参数", default="")
    response_assert = models.TextField("验证", default="")
    create_time = models.DateTimeField("创建时间",auto_now_add=True)

    def __str__(self):
        return self.name


class TestTask(models.Model):
    """
    任务表
    """
    name = models.CharField("名称",max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.IntegerField("状态",default=0)
    cases = models.TextField("关联用例",default="")
    create_time = models.DateTimeField("创建时间",auto_now_add=True)

    def __str__(self):
        return self.name