from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = Recipe.objects.get(id=recipe_id)
    product = Product.objects.get(id=product_id)

    recipe_product, created = RecipeProduct.objects.update_or_create(
        recipe=recipe, product=product, defaults={'weight': weight}
    )

    return HttpResponse("Product added to recipe", status=200)


def cook_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    for recipe_product in RecipeProduct.objects.filter(recipe=recipe):
        product = recipe_product.product
        product.times_used += 1
        product.save()

    return HttpResponse("Recipe cooked", status=200)


def show_recipes_without_product(request, product_id):
    recipes_with_product = RecipeProduct.objects.filter(
        product_id=product_id,
        weight__gte=10
    ).values_list('recipe_id', flat=True)

    recipes = Recipe.objects.exclude(id__in=recipes_with_product)

    return render(request, 'recipes.html', {'recipes': recipes})
