from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

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
    return render(request,'enroll/addandshow.html',{'form':fm})
