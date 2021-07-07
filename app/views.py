from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

# Home page
def home(request):
  return render(request, 'index.html')

# Login Page
def loginuser(request):
  if request.method == "POST":
    fm = AuthenticationForm(data=request.POST)
    if fm.is_valid():
      #print(fm.is_valid())
      username = fm.cleaned_data.get('username')
      password = fm.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user != None:
        #print(user)
        login(request,user)
        return redirect('home')
    else:
        context = {
          "form" : fm
        }
        return render(request , 'login.html' , context=context)
  else:
    fm = AuthenticationForm()
    context = {
      'form':fm,
    }
    return render(request , 'login.html' , context=context )


# Signup Page
def signup(request):
  if request.method == "POST":
    fm = UserCreationForm(request.POST)
    if fm.is_valid():
      messages.success(request,"Account Created!!")
      fm.save()
      #print("user: " , user)
      return redirect("login")
  else:
    fm = UserCreationForm()
    context = {
    'form':fm,
    }
    return render(request,'signup.html',context)
