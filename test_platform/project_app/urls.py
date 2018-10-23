from django.urls import path
from project_app.views import project_views,module_views

urlpatterns = [
    #项目管理
    path('project_manage/', project_views.project_manage),
    path('add_project/',project_views.add_project),
    path('edit_project/<int:pid>/', project_views.edit_project),
    path('del_project/<int:pid>/', project_views.del_project),

    #模块管理
    path('module_manage/', module_views.module_manage),
    path('add_module/', module_views.add_module),
    path('edit_module/<int:pid>/', module_views.edit_module),
    path('del_module/<int:pid>/', module_views.del_module),
]
