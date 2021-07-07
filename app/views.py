from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# Home page
def home(request):
  return render(request, 'index.html')

# Login Page
def login(request):
  return render(request, 'login.html')

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
  return render(request,'signup.html',{'form':fm})
