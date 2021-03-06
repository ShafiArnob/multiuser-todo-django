from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginuser, name='login'),
    path('signup', views.signup, name='signup'),
    path('add-todo', views.add_todo),
    path('logout',views.logout_user, name='logout'),
    path('delete/<int:id>',views.delete_item, name='delete'),
    path('change-status/<int:id>/<str:status>',views.change_status)

]
 