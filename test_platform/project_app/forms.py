from django import forms

#项目表单
class ProjectForm(forms.Form):
    name = forms.CharField(label="项目名称", max_length=1000)
    desc = forms.CharField(label="项目描述", max_length=3000, widget=forms.Textarea)
    status = forms.BooleanField(label="项目状态")