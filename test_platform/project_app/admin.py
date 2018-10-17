from django.contrib import admin
# Register your models here.
from project_app.models import Project, Module
# Register your models here.
# django 自带了一个admin的后台，用于管理前台创建的表



class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'status', 'create_time']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'project_name', 'create_time']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)

