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