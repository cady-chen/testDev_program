from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

#from django.contrib.auth.decorators import login_required


# Create your views here.
#主要代码逻辑


def index(request):
    return render(request, "login.html")

#处理登录请求
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        if username == "" or password == "":
            return render(request, "login.html", {"error": "用户名或密码为空"})  #若用户名或密码为空，则停留在首页并给出提示
        else:
            user = auth.authenticate(username=username, password=password)  #若用户名及密码不为空，则需要获取页面上输入的用户名及密码到数据库里进行验证

            if user is not None:
                auth.login(request, user)  #记录用户登录状态，用于后续的一些模块操作
                #return render(request, "project_manage.html")  #若用户名与密码匹配，则登录成功，跳转至下一个页面
                request.session['user1'] = username #获取登录用户名
                return HttpResponseRedirect('/manage/project_manage/')  #设置跳转对象

            else:
                return render(request, "login.html", {"error": "用户名或密码错误"})  #若用户名与密码不匹配，则给出提示

def logout(request):
    auth.logout(request)  #清除用户的登录信息
    response = HttpResponseRedirect('/') #返回到登录首页
    return response

