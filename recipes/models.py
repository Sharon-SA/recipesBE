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
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class Instructions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    steps = models.IntegerField(blank=False, null=False)
    directions = models.TextField(blank=False)

    def __str__(self):
        return self.directions

    class Meta:
        verbose_name = 'Instruction'
        verbose_name_plural = 'Instructions'


class NutritionalInformation(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    fact = models.CharField(max_length=125)

    def __str__(self):
        return self.fact


class Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=125)
    quantity = models.CharField(max_length=125)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stars = models.IntegerField()
    subject = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_at = timezone.now()
        self.save()

    def updated(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
