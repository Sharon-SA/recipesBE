"""recipes_rest URL Configuration

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

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('category/', views.category_list),
    url(r'^api/category/$', views.category_list),
    url(r'^api/category/(?P<pk>[0-9]+)$', views.getCategory),
    path('cuisine/', views.cuisine_list),
    url(r'^api/cuisine/$', views.cuisine_list),
    url(r'^api/cuisine/(?P<pk>[0-9]+)$', views.getCuisine),
    path('meal/', views.meal_list),
    url(r'^api/meal/$', views.meal_list),
    url(r'^api/meal/(?P<pk>[0-9]+)$', views.getMeal),
    path('diet/', views.diet_list),
    url(r'^api/diet/$', views.diet_list),
    url(r'^api/diet/(?P<pk>[0-9]+)$', views.getDiet),
    path('', views.recipe_list),
    url(r'^api/recipe/$', views.recipe_list),
    url(r'^api/recipe/(?P<pk>[0-9]+)$', views.getRecipe),
    path('register/', views.RegisterView.as_view(), name='auth_register')
]
