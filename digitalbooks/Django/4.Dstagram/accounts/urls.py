from re import template
from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *

#  http://127.0.0.1:8000/accounts/profile/
# 1. profile 만들기
# 2. profile 페이지가 아닌 페이지로 보내기(a. 장고 설정 변경 /b. 웹 서버에서 설정(redirect))

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),     # default : 관리자 페이지 로그아웃 ==> template_name 지정
    path('register/', register, name='register'),
]
