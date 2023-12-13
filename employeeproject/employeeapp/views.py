from django.shortcuts import render
from.forms import Myform

# Create your views here.
def home_view(request):
    form= Myform()
    return render(request,'home.html',{'form':form})

def empdetails(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            empid=form.cleaned_data['empid']
            age=form.cleaned_data['age']
            department=form.cleaned_data['department']
            salary=form.cleaned_data['salary']
            return render(request,"success.html",{'name':name,'empid':empid,'age':age,'department':department,'salary':salary})
    else:
        form=Myform()
        return render(request,"home.html",{'form':form})
