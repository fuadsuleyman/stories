from django.urls import path
from . import views

from .views import (
    RecipeListView,
    index,
    about,
    stories,
)

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='stories-index'),
    path('about/', views.about, name='stories-about'),
    path('stories/', views.stories, name='stories-stories'),
    # path('contact/', views.contact, name='stories-contact'),
    path('recipes/', RecipeListView.as_view(), name='stories-recipes'),
    # path('recipes/', views.recipes, name='stories-recipes'),
]
