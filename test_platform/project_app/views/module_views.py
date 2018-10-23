from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import AddModuleForm,EditModuleForm
from django.http import HttpResponseRedirect

# Create your views here.

@login_required #判断用户是否已经登录，如果未登录，在浏览器中直接输入project_manage的地址，不让访问
#模块列表管理
def module_manage(request):
    module_list = Module.objects.all()
    username = request.session.get('user1', '')
    return render(request, "module_manage.html", {"user": username, "modules": module_list, "type": 'list'})


#添加模块
@login_required
def add_module(request):
    if request.method == 'POST':
        form = AddModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            project_name = form.cleaned_data['project_name']
            Module.objects.create(name=name, desc=desc,project_name=project_name)
            return redirect('/manage/module_manage/')
    else:
        form = AddModuleForm()

    return render(request,"module_manage.html",{"form": form, "type": "add"})


#编辑模块
@login_required
def edit_module(request,pid):
    if request.method == 'POST':
        form = EditModuleForm(request.POST)
        if form.is_valid():
            model = Module.objects.get(id=pid)
            model.name = form.cleaned_data['name']
            model.desc = form.cleaned_data['desc']
            model.project_name = form.cleaned_data['project_name']
            model.save()
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        #判断pid是否有传入,若有传入则
        if pid:
            form = EditModuleForm(instance=Module.objects.get(id=pid))
    return render(request,'module_manage.html', {'form': form, 'type': "edit"})


#删除模块
@login_required
def del_module(request, pid):
    Module.objects.get(id=pid).delete()
    return HttpResponseRedirect("/manage/module_manage/")