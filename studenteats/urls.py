from django.urls import path
from django.urls import re_path
from studenteats import views 

app_name = 'studenteats'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/<username>/',views.ProfileView.as_view(),name='profile'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/update/$', views.profile_update, name='profile_update'),
    #re_path(r'^studenteats/profile/$', views.profile, name='profile'),
    #re_path(r'^profile/update/$',views.profile_update, name='profile_update'),
    #re_path(r'^studenteats/profile_update/$', views.profile_update, name='profile_update'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('recipe/', views.recipe, name='recipe'),
    path('about', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    path('help/', views.help, name='help'),
]
