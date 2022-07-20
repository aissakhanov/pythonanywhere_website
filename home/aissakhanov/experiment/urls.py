"""experiment URL Configuration

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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ml_algorithms/', views.ml_algorithms, name='ml_algorithms'),
    path('num_methods/', views.num_methods, name='num_methods'),
    path('supervised_learning/',views.supervised_learning, name='supervised_learning'),
    path('linear_regression/',views.lin_reg, name='lin_reg'),
    path('root_finding/', views.root_finding, name='root_finding'),
    path('bis_method/', views.bis_method, name='bis_method'),
    path('sorting_algorithms/', views.sort_alg, name='sort_algo'),
    path('bubble_sort/', views.bubble_sort, name='bubble_sort'),
    path('selection_sort/', views.selection_sort, name='selection_sort')
]
