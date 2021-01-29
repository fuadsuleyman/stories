from django import template

register = template.Library()

from stories.models import Category

# categories = Category.objects.all()

# categories_list = []

# for i in categories:
#     categories_list.append(i.title)

# print(categories_list)

# categories_list = ['Fruits', 'Vegetables', 'Protein', 'Dairy']

@register.simple_tag
def get_categories():
    return Category.objects.filter(is_published=True)[0:3]