from django import forms

class Myform(forms.Form):
    name=forms.CharField(max_length=20)
    empid=forms.CharField(max_length=12)
    age=forms.IntegerField()
    department=forms.CharField(max_length=50)
    salary=forms.CharField(max_length=20)