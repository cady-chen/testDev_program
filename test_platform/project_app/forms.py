from django import forms
from .models import Project,Module

#项目表单
#class ProjectForm(forms.Form):
#    name = forms.CharField(label="项目名称", max_length=1000)
#    desc = forms.CharField(label="项目描述", max_length=3000, widget=forms.Textarea)
#    status = forms.BooleanField(label="项目状态")


class AddProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'desc']
        #exclude = ['status','create_time'] 实现的功能与上一句一样，exclude就是除了后面的这个字段不展示，其它都展示的意思


class EditProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ['create_time']


class AddModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['name', 'desc', 'project_name']


class EditModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        exclude = ['create_time']