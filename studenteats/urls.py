from django.urls import path
from studenteats import views 

app_name = 'studenteats'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('restaurant/', views.restaurant, name='restaurant'), 
    path('recipe/', views.recipe, name='recipe'),
    path('about', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    path('help/', views.help, name='help'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('show_recipes/<int:Recipe_id>/',views.show_recipes, name='show_recipes')
]
