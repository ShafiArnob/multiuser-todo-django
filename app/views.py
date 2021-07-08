from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import TODO
from .forms import TODOForm
# Create your views here.

# Home page
def home(request):
  if request.user.is_authenticated:
    user = request.user
    form = TODOForm()
    todos = TODO.objects.filter(user=user)
    return render(request, 'index.html', {'form':form,'todos':todos})

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


# 
def add_todo(request):
  # check if the user is logged in 
  if request.user.is_authenticated:
    user = request.user # gets the user
    print(user)
    fm = TODOForm(request.POST)
    if fm.is_valid():
      print(fm.cleaned_data)
      todo = fm.save(commit=False)
      todo.user = user
      todo.save()
      print(todo)
      return redirect("home")
    else:
      return render(request,'index.html', context={'form':fm})