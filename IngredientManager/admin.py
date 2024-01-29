from django.contrib import admin
from .models import *


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeProductInline,)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product)
