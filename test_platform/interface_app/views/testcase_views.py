import json
import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect
#导入三个模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from interface_app.models import TestCase
from interface_app.forms import TestCaseForm


# Create your views here.


#获取用例例表
def case_manage(request):
    testcases = TestCase.objects.all().order_by("id") #查询结果集
    #定义页面上展示5条用例
    paginator = Paginator(testcases, 5) #实例化结果集，每页展示5条数据
    page = request.GET.get('page') #接收网页中的page值
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果页数不是整型，取第一页
        contacts = paginator.page(1)
    except EmptyPage:
        #如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        return render(request, "case_manage.html",
                      {"type": "list",
                       "testcases": contacts,
                       })
    else:
        return HttpResponse("404")

#根据用例名称搜索
def search_case_name(request):

    if request.method == "GET":
        case_name = request.GET.get('case_name', "")
        cases = TestCase.objects.filter(name__contains=case_name)
        paginator = Paginator(cases, 10)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # 如果页数不是整型，取第一页
            contacts = paginator.page(1)
        except EmptyPage:
            # 如果页数超出查询范围，取最后一页
            contacts = paginator.page(paginator.num_pages)

        return render(request, "case_manage.html",{
            "type": "list",
            "testcases": contacts,
            "case_name": case_name,
        })
    else:
        return HttpResponse("404")


#创建接口测试用例
def add_case(request):
    if request.method == "GET":
        return render(request, "add_case.html", {
            "type": "add"
        })
    else:
        return HttpResponse("404")

#编辑接口测试用例
def debug_case(request, cid):
    if request.method == "GET":
        return render(request, "debug_case.html",{
            "type": "debug"
        })
    else:
        return HttpResponse("404")


def debug(request):
    if request.method == "GET":
        form = TestCaseForm()
        return render(request, "api_debug.html", {"form": form, "type": "debug"})
    else:
        return HttpResponse("404")

#调试接口
def api_debug(request):
    if request.method == 'POST':
        url = request.POST.get("req_url")
        method = request.POST.get("req_method")
        parameter = request.POST.get("req_parameter")
        if method == "get":
            r = requests.get(url, params=parameter)
        if method == "post":
            r = requests.post(url, json=parameter)
        return HttpResponse(r.text)
    else:
        return render(request, "api_debug.html", {"type": "debug"})


#删除用例
@login_required
def delete_case(request,cid):
    TestCase.objects.get(id=cid).delete()
    return HttpResponseRedirect("/interface/case_manage/")



