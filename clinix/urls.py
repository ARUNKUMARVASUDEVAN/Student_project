"""
URL configuration for clinix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from backend.views import home_page,user_registration,dashboard_view,upload_test_information,test_request,test_report,upload_result

from backend import views 
from backend.forms import LoginForm
urlpatterns = [
    path("admin/", admin.site.urls),
    path('home_page/',home_page,name='GCLRAShomepage'),
    path('dashboard/',dashboard_view,name='dashboard'),
    path('',home_page,name='GCLRAShomepage'),
    path('registration/',user_registration,name='User_registration_page'),
    path('authentication/',auth_views.LoginView.as_view(template_name='backend/authentication.html',authentication_form=LoginForm),name='authentication'),
    path('upload_test_info/',upload_test_information,name='upload_test_information'),
    path('test_request/',test_request,name='test_request'),
    path('test_report/',test_report,name='test_report'),
    path('upload_result/',upload_result,name='upload_result')
]
