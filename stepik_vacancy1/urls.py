"""stepik_vacancy1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from vacancy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('vacancies/', views.vacancies_view, name='vacancies'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_view, name='vacancy'),
    path('companies/<int:company_id>/', views.company_view, name='company'),
    path('companies/', views.companies_view, name='companies'),
    path('vacancies/cat/<str:speciality_code>/', views.speciality_view, name='speciality')
]
