from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect

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
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            Project.objects.create(name=name, desc=desc)
            return redirect('/manage/project_manage')
    else:
        form = ProjectForm()

    return render(request,"project_manage.html",{"form": form, "type": "add"})


#编辑项目
@login_required
def edit_project(request,pid):
    project_obj = Project.objects.get(id=pid)
    if request.method == 'POST':
        form = ProjectForm(request.POST,isinstance= project_obj)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            status = form.cleaned_data['status']
            form.save()
            return HttpResponseRedirect('/manage/project_manage')
    else:
        form = ProjectForm()
    return render(request,'project_manage.html', {'form': form, 'type': "edit"})

