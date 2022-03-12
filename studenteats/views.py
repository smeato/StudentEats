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
    Recipe_List=Recipe.objects.all()
    Most_Popular_Recipe_List=Recipe.objects.order_by('Likes')[0:10]


    context_dict = {'Recipe':Recipe_List,'Most_Popular_Recipe':Most_Popular_Recipe_List}
    return render(request, 'studenteats/recipe.html', context=context_dict)

def search_recipes(request):
    if request.method =="POST":
        searched=request.POST['searched']
        recipts=Recipe.objects.filter(Cuisine__contains=searched)

        return render(request, 'studenteats/events/search_recipes.html', {'searched':searched,'recipts':recipts})

    return render(request, 'studenteats/events/search_recipes.html', {})

def show_recipes(request,Recipe_id):
    recipe=Recipe.objects.filter(Recipe(Recipe_ID=Recipe_id))
    context_dict = {}
    context_dict['Recipe']=recipe
    return render(request, 'studenteats/events/show_recipes.html', context_dict)


def forum(request): 

    Discussion_List = Discussion.objects.all()
    context_dict = {}
    context_dict['Discussions']=Discussion_List

    return render(request, 'studenteats/forum.html', context=context_dict)

def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)