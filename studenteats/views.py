from django.shortcuts import render
from studenteats.models import User,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments

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

def recipe(request): 
    context_dict = {}
    return render(request, 'studenteats/recipe.html', context=context_dict)

def forum(request): 
    context_dict = {}
    return render(request, 'studenteats/forum.html', context=context_dict)

def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)