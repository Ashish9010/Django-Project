"""Admission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Student_info.views import view_Student,view_data
from Student_info.views import view_Admission,view_Marks,view_Feedback,view_home,view_navi,view_eg;
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', view_Student),
    path('admission/', view_Admission),
    path('mark/', view_Marks),
    path('feedback/', view_Feedback),
    path('home/', view_home),
    path('', view_navi,name="add_student"),
    path('eg/', view_eg),
    path('data/', view_data),
    # path('',include('Student_info.urls'))
    
]
