from django.contrib import admin
from django.urls import path, re_path

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from recipes import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('category/', views.category_list),
    re_path(r'^api/category/$', views.category_list),
    re_path(r'^api/category/(?P<pk>[0-9]+)$', views.getCategory),
    path('cuisine/', views.cuisine_list),
    re_path(r'^api/cuisine/$', views.cuisine_list),
    re_path(r'^api/cuisine/(?P<pk>[0-9]+)$', views.getCuisine),
    path('meal/', views.meal_list),
    re_path(r'^api/meal/$', views.meal_list),
    re_path(r'^api/meal/(?P<pk>[0-9]+)$', views.getMeal),
    path('diet/', views.diet_list),
    re_path(r'^api/diet/$', views.diet_list),
    re_path(r'^api/diet/(?P<pk>[0-9]+)$', views.getDiet),
    path('', views.recipe_list),
    re_path(r'^api/recipe/$', views.recipe_list),
    re_path(r'^api/recipe/(?P<pk>[0-9]+)$', views.getRecipe),
    path('instructions/', views.instructions_list),
    re_path(r'^api/instructions/$', views.instructions_list),
    re_path(r'^api/instructions/(?P<pk>[0-9]+)$', views.getInstructions),
    path('nutrition/', views.nutrition_list),
    re_path(r'^api/nutrition/$', views.nutrition_list),
    re_path(r'^api/nutrition/(?P<pk>[0-9]+)$', views.getNutrition),
    path('ingredients/', views.ingredients_list),
    re_path(r'^api/ingredients/$', views.ingredients_list),
    re_path(r'^api/ingredients/(?P<pk>[0-9]+)$', views.getIngredients),
    path('comments/', views.comments_list),
    re_path(r'^api/comments/$', views.comments_list),
    re_path(r'^api/comments/(?P<pk>[0-9]+)$', views.getComments),
    path('favorites/', views.favorites_list),
    re_path(r'^api/favorites/$', views.favorites_list),
    re_path(r'^api/favorites/(?P<pk>[0-9]+)$', views.getFavorites),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
]

