from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#主要代码逻辑


def index(request):
    return render(request, "login.html")

#处理登录请求
def login_action(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        password = request.GET.get("password")

        if username == "" or password == "":
            return render(request, "login.html", {"error": "用户名或密码错误"} )
