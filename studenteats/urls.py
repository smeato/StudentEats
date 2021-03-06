from django.urls import path
from studenteats import views
from studenteats.models import Discussion_Replies 

app_name = 'studenteats'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<username>/',views.ProfileView.as_view(),name='profile'),
    path('profile/', views.profile, name='profile'),
    
    path('restaurant/', views.restaurant, name='restaurant'), 
    path('restaurant/<place>/', views.getCoordinates, name='get-coordinates'),
    path('recipe/', views.recipeHome, name='recipe'),
    path('about', views.about, name='about'),
    path('forum/', views.forum, name='forum'),
    path('help/', views.help, name='help'),
    path('discussion_detail/<int:discussion_ID>',views.discussion_detail,name='discussion_detail'),
    path('forum/<int:state>',views.forum,name='forum'),
    path('add_comments/',views.add_comments,name='add_comments'),
    path('save_comments/',views.save_comments,name='save_comments'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('search_restaurants/', views.search_restaurants, name='search_restaurants'),
    path('show_restaurants/<int:Restaurant_id>/',views.show_restaurants, name='show_restaurants'),
    path('discussion_detail/<int:discussion_ID>',views.discussion_detail,name='discussion_detail'),
    path('show_recipes/<int:Recipe_id>/',views.show_recipes, name='show_recipes'),
    path('add-recipe/', views.addRecipe, name='add-recipe'),
    path('delete-recipes/<int:id>', views.deleteRecipe, name='delete-recipe'),
    path('show_recipes/<int:id>/<int:value>/', views.updateLikes, name='update-likes'),
    path('show_restaurants/<int:id>/<int:value>/', views.updateLikes, name='update-likes')
    ]
