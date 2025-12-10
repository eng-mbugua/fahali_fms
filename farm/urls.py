"""
URL configuration for fahali project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views

from farm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #Crops
    path('crops/', views.crops, name='crops'),
    path('add_crop', views.add_crop, name='add_crop'),
    path('delete_crop/<int:id>/', views.delete_crop, name='delete_crop'),
    path('edit_crop/<int:crop_id>/', views.edit_crop, name='edit_crop'),


    #Livestock
    path('livestock/', views.livestock, name='livestock'),
    path('add_livestock', views.add_livestock, name='add_livestock'),
    path('edit_livestock<int:animal_id>/', views.edit_livestock, name='edit_livestock'),
    path('delete_livestock/<int:id>/', views.delete_livestock, name='delete_livestock'),
    # path('livestock/add/', views.add_livestock, name='add_livestock'),
    # path('livestock/delete/<int:animal_id>/', views.delete_livestock, name='delete_livestock'),

    #Resources
    path('resources/', views.resources, name='resources'),
    path('add_resource', views.add_resource, name='add_resource'),
    path('delete_resource/<int:id>/', views.delete_resource, name='delete_resource'),


    #Veterinarian
    path('vet/', views.vet, name='vet'),
    path('add_vet_record', views.add_vet_record, name='add_vet_record'),
    path('delete_vet_record/<int:id>/', views.delete_vet_record, name='delete_vet_record'),

    #Financials
    path ('financials/', views.financials, name='financials'),
    path('financials/add/', views.add_financial, name='add_financial'),
    path('financials/delete/<int:fin_id>/', views.delete_financial, name='delete_financial'),


    #Marketplace
    path('marketplace/', views.marketplace, name='marketplace'),



]
