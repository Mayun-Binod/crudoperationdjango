from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


# this function will add new item and show all item
def add_show(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save() one method
            # another method
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            res=User(name=nm,email=em,password=pw)
            # res=User(name=nm,email=em) # if you don't want to show in databases of password
            res.save()
            fm=StudentRegistration() # to blank just like reset the information of forms

    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


# this function will delete 
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi) 
    return render(request,'enroll/updatestudent.html',{'form':fm})

