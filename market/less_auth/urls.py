from django.urls import path

from .views import login_my, exit_my_account, my_regis

urlpatterns = [
    path('', login_my, name='login'),
    path("exit/", exit_my_account, name='logout'),
    path("my_regis/", my_regis, name='regis'),
    
]
