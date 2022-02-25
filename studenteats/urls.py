from django.urls import path
from studenteats import views 

app_name = 'studenteats'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('restricted/',views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.profile, name='profile'),
    path('restaurant/', views.restaurant, name='restaurant'), 
    path('recipe/', views.recipe, name='recipe'),
    path('about/', views.about, name='about'),
    #path('form/', views.forum, name='form'),
    
]
