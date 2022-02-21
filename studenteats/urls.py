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
    path('forum/', views.forum, name='forum')
]
