from django.shortcuts import render, get_object_or_404
from studenteats.models import UserProfile,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator
from studenteats.forms import UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

# Create your views here.
def index(request): 
    context_dict = {}
    return render(request, 'studenteats/index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'studenteats/login.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('studenteats:index'))
            else:
                return HttpResponse("Your Account account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'studenteats/login.html')

        
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('studenteats:index'))

def some_view(request):
    
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
        
class ProfileView(View):
    def get_user_details(self,username):
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
           return None
        user_profile=UserProfile.objects.get_or_create(user=user)[0]
        form=UserProfileForm({'website':user_profile.website,'picture':user_profile.picture})
        
        return(user,user_profile,form)
        
    @method_decorator(login_required)
    def get(self,request,username):
        try:
            (user,user_profile,form)=self.get_user_details(username)
        except TypeError:
            return redirect(reverse('studenteats:index'))
            
        context_dict={'user_profile':user_profile,
                     'selected_user':user,
                     'form':form}
                    
        return render(request,'studenteats/profile.html',context_dict)
        
    @method_decorator(login_required)
    def post(self,request,username):
        try:
            (user,user_profile, form)= self.get_user_details(username)
        except TypeError:
            return redirect(reverse('student:index'))
            
        form = UserProfileForm(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('studenteats:profile',user.username)
        else:
            print(form.errors)
        
        context_dict = {'user_profile':user_profile,
                     'selected_user':user,
                     'form':form}
                     
        return render(request,'studenteats/profile.html',context_dict)
                     


@login_required
def profile(request):
    if request.method=="POST":
        form=UserProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            username=request.user.username
            #message.success(request,f'{username},Your Profile is update.')
            return redirect('/')
        else:
            form=UserProfileForm(instance=request.user.profile)
        context={'form':form}
        return render(request,'studenteats/profile.html',context)
    #context_dict = {}
    #user=get_object_or_404(User)
    #user= request.user
    #return render(request, 'studenteats/profile.html',{'user':user})
    #return render(request, 'studenteats/profile.html', context=context_dict)


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

    Discussion_List = Discussion.objects.all()
    context_dict = {}
    context_dict['Discussions']=Discussion_List

    return render(request, 'studenteats/forum.html', context=context_dict)

def help(request): 
    context_dict = {} 
    return render(request, 'studenteats/help.html', context=context_dict)
