from .models import CustomUser
from django.contrib import messages
from django.shortcuts import render,redirect



def must_register_before_login(my_view):#we can write anything  in myview its just name
    def gatekeeper(request,*args,**kwargs):
        if CustomUser.objects.count() == 0:
            messages.info(request,'Please Register before login')
            return redirect('register')
        return my_view(request,*args,*kwargs)
    return gatekeeper