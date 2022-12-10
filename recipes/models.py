from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cuisine_name

    class Meta:
        verbose_name = 'Cuisine'
        verbose_name_plural = 'Cuisines'


class Meal(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Diet(models.Model):
    diet_name = models.CharField(max_length=100)

    def __str__(self):
        return self.diet_name

    class Meta:
        verbose_name = 'Diet'
        verbose_name_plural = 'Diets'


class Recipe(models.Model):
    title = models.CharField(max_length=250)
    image_url = models.URLField()
    stars = models.FloatField()
    ready_in_minutes = models.IntegerField(blank=False, null=False)
    servings = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
