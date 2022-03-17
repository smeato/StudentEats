from email.policy import default
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

def forum(request,state=0): 

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
    try:
        discussion=Discussion.objects.get(Discussion_ID=discussion_ID)
        reply=Discussion_Replies.objects.filter(Discussion_ID=discussion_ID)
    except Discussion.DoesNotExist:
        discussion = None
    context_dict={'discussion':discussion}
    context_dict={'reply':reply}


    return render(request,'studenteats/discussion_detail.html',context=context_dict)


def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)