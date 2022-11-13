from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Cuisine, Meal, Diet, Recipe, Instructions, NutritionalInformation, Ingredients, Comments, \
    Favorites


class CommentInline(admin.TabularInline):
    model = Comments


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'ready_in_minutes', 'servings', 'price', 'cuisine', 'category', 'meal', 'diet')
    list_filter = ('title', 'ready_in_minutes', 'servings', 'price', 'cuisine', 'category', 'meal', 'diet')
    search_fields = ('title', 'ready_in_minutes', 'servings', 'price', 'cuisine', 'category', 'meal', 'diet')
    ordering = ['cuisine']


class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'steps', 'directions')


class NutritionalAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'fact')


admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Diet)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Instructions, InstructionsAdmin)
admin.site.register(NutritionalInformation, NutritionalAdmin)
admin.site.register(Ingredients)
admin.site.register(Comments)
admin.site.register(Favorites)
