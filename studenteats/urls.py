from django.urls import path
from studenteats import views
from studenteats.models import Discussion_Replies 

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
    path('discussion_detail/<int:discussion_ID>',views.discussion_detail,name='discussion_detail')
]
