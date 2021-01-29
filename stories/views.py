from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Story, Category, Recipe, Author
from .forms import ContactForm
from django.contrib import messages 

# Create your views here.

# def home(request):
#     context = {
#         'stories': Story.objects.all(),
#         'recipes': Recipe.obects.all()
#     }
#     return render(request, 'stories/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Mesajiniz gonderildi, tezlikle sizinle elaqe saxlanilacaq!')
            return redirect('stories-index')
    else:
        form = ContactForm
    return render(request, 'stories/contact.html', {'form': form})


about_page_data = {
        'page_title': 'About Us',
        'description_text': 'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia',
        'daily_dates': [
            {'key1': 'visitors', 'count': '100'},
            {'key1': 'stories', 'count': '200'},
            {'key1': 'recipes', 'count': '300'},
            {'key1': 'users', 'count': '40'},
            ]
    }


def index(request):
    
    stories = Story.objects.all()
    # categories = Category.objects.filter(is_published=True)[0:3]
    recipes = Recipe.objects.all()

    paginate_by = 2

    context = {
        'stories': stories, 'recipes': recipes
    }
    return render(request, 'stories/index.html', context)




def about(request):
    return render(request, 'stories/about.html')

###########################################################

def home(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'stories/recipes.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'stories/recipes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'recipes'
    # ordering = ['-date_posted']
    paginate_by = 5

# def recipes(request):
#     recipes = Recipe.objects.all()
#     context = {
#         'recipes': recipes
#     }
#     return render(request, 'stories/recipes.html', context)

############################################################

def stories(request):
    stories = Story.objects.all()
    categories = Category.objects.filter(is_published=True)[0:3]

    context = {
        'stories': stories, 'categories': categories
    }

    return render(request, 'stories/stories.html', context)