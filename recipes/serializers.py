from .models import Category, Cuisine, Meal, Diet, Recipe, Instructions, NutritionalInformation, Ingredients, Comments, Favorites
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'category_name')


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ('pk', 'cuisine_name')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('pk', 'type')


class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ('pk', 'diet_name')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('pk', 'title', 'image_url', 'stars', 'ready_in_minutes', 'servings', 'price', 'cuisine', 'category', 'meal', 'diet')


class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructions
        fields = ('pk', 'recipe', 'steps', 'directions')


class NutritionalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalInformation
        fields = ('pk', 'recipe', 'fact')


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('pk', 'recipe', 'ingredient_name', 'quantity')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('pk', 'user', 'recipe', 'stars', 'subject', 'body', 'created_at', 'updated_at')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('pk', 'user', 'recipe')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'min_length': 6},
            'password2': {'write_only': True, 'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
