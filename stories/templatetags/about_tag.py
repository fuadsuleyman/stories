from django import template

register = template.Library()

from stories.models import Story, Recipe, Author

all_recipes = Recipe.objects.all()
recipe_count = all_recipes.count()

all_stories = Story.objects.all()
stories_count = all_stories.count()

all_users = Author.objects.all()
users_count = all_users.count()
# 'daily_dates': [
#             {'key1': 'visitors', 'count': '100'},
#             {'key1': 'stories', 'count': '200'},
#             {'key1': 'recipes', 'count': '300'},
#             {'key1': 'users', 'count': '40'},
#             ]
my_about_data = []
my_about_data.append(recipe_count)
my_about_data.append(stories_count)
my_about_data.append(users_count)
# about_page_data = {
#         'daily_dates':[
#             {'key1': 'Visitors', 'count': '100'},
#             {'key1': 'Stories', 'count': stories_count },
#             {'key1': 'Recipes', 'count': recipe_count },
#             {'key1': 'Users', 'count': all_users},
#         ]
# }

about_page_data = {
        'page_title': 'About Us',
        'description_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia',
        'daily_dates': [
            {'key1': 'visitors', 'count': '100'},
            {'key1': 'stories', 'count': stories_count},
            {'key1': 'recipes', 'count': recipe_count},
            {'key1': 'users', 'count': users_count},
            ]
    }


@register.simple_tag
def get_about_data():
    return about_page_data