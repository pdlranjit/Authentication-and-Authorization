from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserForm,LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .decorators import must_register_before_login

def register_view(request):
    if request.method== "POST":
        form= CustomUserForm(request.POST)
        if form.is_valid(): #is saves  user in Databse with cystomfields
         form.save()
         return redirect('register')
    else:
       form=CustomUserForm()
    return render(request,'authentication/register.html',{'form':form})
@must_register_before_login
#
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Trying to find user by email not username
            try:
                user_obj = CustomUser.objects.get(email=email)# i have  try to find username with email so i need this if i dont need this  i can  do by default like 
                user = authenticate(request, username=user_obj.username, password=password)

                if user is not None:
                    login(request, user)
                    return render(request,'authentication/success.html')
                else:
                    messages.error(request, 'Invalid email or password.')

            except CustomUser.DoesNotExist:
                messages.error(request, 'No account found with this email.')
    else:
        form = LoginForm()
    
    
    return render(request, 'authentication/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('register')

   
   
