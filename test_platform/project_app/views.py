from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app import Project


# Create your views here.

@login_required #判断用户是否已经登录，如果未登录，在浏览器中直接输入project_manage的地址，不让访问
#项目列表管理
def project_manage(request):
    project_list = Project.objects.all()
    username = request.session.get('user1', '')
    return render(request, "project_manage.html", {"user": username, "projects": project_list, "type": 'list'})


#添加项目
@login_required
def add_project(request):
     return render(request,"project_manage.html",{"type": "add"})
