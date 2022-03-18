from django.db.models import Q
from studenteats.models import AdminDetails, User,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments
import datetime
from email.policy import default
from django.forms import DateField
from django.shortcuts import redirect, render
from django.urls import reverse

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
    #context_dict['recipeWeek'] = AdminDetails.objects.first().recipeWeek
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


def forum(request, state=0): 
    Discussion_like = Discussion.objects.order_by('-Likes')[:3]
    Discussion_view = Discussion.objects.order_by('-Views')[:3]
    Discussion_createdtime = Discussion.objects.order_by('-Created_Time')[:3]
    
    context_dict = {}

    if (state==0):
        context_dict['Discussions']=Discussion_like
    elif(state==1):
        context_dict['Discussions']=Discussion_view
    else:
        context_dict['Discussions']=Discussion_createdtime

    return render(request, 'studenteats/forum.html', context=context_dict)

def discussion_detail(request,discussion_ID):

    discussion=Discussion.objects.filter(Discussion_ID=discussion_ID)
    reply=Discussion_Replies.objects.filter(Discussion_ID=discussion_ID)
    discussion=list(discussion)
    reply=list(reply)

    context_dict={}
    context_dict={'discussion':discussion,'reply':reply}
    current_discussion=discussion[0].Discussion_ID 
    request.session['diss_id'] = current_discussion #设置diss_id 存到session里

    print(context_dict)

    return render(request,'studenteats/discussion_detail.html',context=context_dict)

def add_comments(request):
    # dission=Discussion.objects.get(Discussion_ID = discussion_ID)
    # diss_id = dission.Discussion_ID
    # user_id = dission.User_ID
    # context_dict={}
    # context_dict={'diss_id':diss_id,'user_id':user_id}
    # return render(request,'studenteats/add_comments.html',context=context_dict)
    diss_id=request.session.get('diss_id')
    user_id=request.user.id
    context_dict={}
    context_dict={'diss_id':diss_id,'user_id':user_id}
    return render(request,'studenteats/add_comments.html',context=context_dict)

def save_comments(request):
    if request.method =="POST":
        diss_id=request.session.get('diss_id')
        user_id=request.user.id
        rep_id=request.POST.get('rep_id')
        #title=request.POST.get('title')
        description=request.POST.get('description')
        create_time=DateField()
        likes=0.0
        #必须登录才能获取到user_id
        reply=Discussion_Replies(Description=description,User_ID=user_id,Created_Time=create_time,Likes=likes,Post_ID=rep_id,Discussion_ID=diss_id)

        return redirect(reverse('studenteats:forum'))
    else:
        return redirect(reverse('studenteats:forum'))


def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)