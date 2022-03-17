from django.shortcuts import render
from django.db.models import Q
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

def recipe(request): 
    Recipe_List=Recipe.objects.all()
    Most_Popular_Recipe_List=Recipe.objects.order_by('Likes')[0:10]
    context_dict = {'Recipe':Recipe_List,'Most_Popular_Recipe':Most_Popular_Recipe_List}
    return render(request, 'studenteats/recipe.html', context=context_dict)

def recipeHome(request): 
    context_dict = {}
    context_dict['popular_recipes'] = Recipe.objects.order_by('Likes')[0:6]
    context_dict['recipeWeek'] = AdminDetails.objects.first().recipeWeek
    context_dict['search'] = Recipe.objects.all()
    return render(request, 'studenteats/recipeHome.html', context=context_dict)

def search_recipes(request):
    if request.method =="POST":
        if request.POST['searched'] != '':
            searched=request.POST['searched']
            recipes=Recipe.objects.filter(Q(Title__icontains=searched) |
            Q(Cuisine__icontains=searched) |
            Q(Tags__icontains=searched))
            context_dict={}
            context_dict['searched']=searched
            context_dict['recipes']=list(recipes.all())
            return render(request, 'studenteats/search_recipes.html', context_dict)
    return recipeHome(request)

def show_recipes(request,Recipe_id):
    print(Recipe_id)
    recipe=Recipe.objects.filter(Recipe_ID=Recipe_id)
    print(recipe)
    context_dict = {}
    context_dict['recipe']=list(recipe)[0]# only one recipe is to be displayed
    return render(request, 'studenteats/events/show_recipes.html', context_dict)


def forum(request): 
    Discussion_like = Discussion.objects.order_by('-Likes')[:3]
    Discussion_view = Discussion.objects.order_by('-Views')[:3]
    Discussion_createdtime = Discussion.objects.order_by('-Created_Time')[:3]
    context_dict = {}
    context_dict['Discussionslike']=Discussion_like
    context_dict['Discussionsview']=Discussion_view
    context_dict['Discussionscreatetime']=Discussion_createdtime
    return render(request, 'studenteats/forum.html', context=context_dict)

def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)