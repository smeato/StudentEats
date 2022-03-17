from django.shortcuts import render
from studenteats.models import AdminDetails, User,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments

# Create your views here.
def index(request): 
    context_dict = {}
    return render(request, 'studenteats/index.html', context=context_dict)

def login(request): 
    context_dict = {}
    return render(request, 'studenteats/login.html', context=context_dict)

def profile(request):
    context_dict = {} 
    return render(request, 'studenteats/profile.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'studenteats/about.html', context=context_dict)

def restaurant(request): 
    context_dict = {}
    return render(request, 'studenteats/restaurant.html', context=context_dict)

def recipeHome(request): 
    context_dict = {}
    context_dict['popular_recipes'] = Recipe.objects.order_by('Likes')[0:6]
    context_dict['recipeWeek'] = AdminDetails.objects.first().recipeWeek
    context_dict['search'] = Recipe.objects.all()
    return render(request, 'studenteats/recipeHome.html', context=context_dict)

def forum(request): 

    Discussion_List = Discussion.objects.all()
    context_dict = {}
    context_dict['Discussions']=Discussion_List

    return render(request, 'studenteats/forum.html', context=context_dict)

def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)