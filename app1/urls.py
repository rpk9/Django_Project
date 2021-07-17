from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('hello', views.func1),
    #path('index',views.index),
    path('',views.index),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('home/<int:id>',views.home, name='home'),
    path('update/<int:id>',views.update, name='update'),
    path('changePassword/<int:id>',views.changePassword, name='changePassword'),
    path('logout',views.logout,name='logout'),
    
]