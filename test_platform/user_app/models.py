from django.db import models
from django.contrib import admin
# Create your models here.
#ORM 该模块是用于创建数据库表


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(User,UserAdmin)


#项目表
class ProjectInfo(models.Model):
    title = models.CharField(u"项目名称", blank=False,max_length=1000)
    desc = models.CharField(u"项目描述",blank=True, max_length=5000)
    status = models.BooleanField(u"项目状态", default=0) #-1代表已作废
    create_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, default="")
    create_time = models.DateTimeField(u"创建时间", auto_now_add=True, blank=True)

    def __str__(self):
        return "{}.{}".format(self.title, self.desc)
