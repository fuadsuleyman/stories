from django.contrib import admin

# Register your models here.

from .models import Recipe, Story, Author, Category, RecipeComment, Tag, Contact

admin.site.register(Recipe)
admin.site.register(Story)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(RecipeComment)
admin.site.register(Tag)
admin.site.register(Contact)