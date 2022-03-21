
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.db.models import F
from django.forms import DateField
from studenteats.models import AdminDetails, User, Recipe, Restaurant, Deals, Discussion, Discussion_Replies, Restaurant_Comments, Recipe_Comments
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import DateField
from studenteats.models import AdminDetails, UserProfile, Recipe, Restaurant, Deals, Discussion, Discussion_Replies, Restaurant_Comments, Recipe_Comments
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.utils.decorators import method_decorator
from studenteats.forms import UserForm, UserProfileForm
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
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm(
            {'website': user_profile.website, 'picture': user_profile.picture})

        return(user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
            recipes = Recipe.objects.filter(Owner__id=request.user.id)

        except TypeError:
            return redirect(reverse('studenteats:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form,
                        'recipes': recipes}

        return render(request, 'studenteats/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('student:index'))

        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        recipes = Recipe.objects.filter(Owner__id=request.user.id)

        if form.is_valid():
            form.save(commit=True)
            return redirect('studenteats:profile', user.username)
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form,
                        'recipes': recipes}

        return render(request, 'studenteats/profile.html', context_dict)


@login_required
def profile(request):
    print(request)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES,
                               instance=request.user.profile)
        recipes = Recipe.objects.filter(Owner__id=request.user.id)

        if form.is_valid():
            form.save()
            username = request.user.username
            #message.success(request,f'{username},Your Profile is update.')
            return redirect('/')
        else:
            form = UserProfileForm(instance=request.user.profile)

        return render(request, 'studenteats/profile.html', {'form': form, 'recipes':recipes})


def about(request):
    context_dict = {}
    return render(request, 'studenteats/about.html', context=context_dict)


def restaurant(request):
    context_dict = {}
    context_dict['popular_restaurants'] = Restaurant.objects.order_by('Likes')[
        0:6]
    if AdminDetails.objects.first() != None:
        context_dict['restaurantWeek'] = AdminDetails.objects.first(
        ).restaurantWeek
    context_dict['search'] = Restaurant.objects.all()
    return render(request, 'studenteats/restaurant.html', context=context_dict)


# def recipe(request):
#     Recipe_List = Recipe.objects.all()
#     Most_Popular_Recipe_List = Recipe.objects.order_by('Likes')[0:10]
#     context_dict = {'Recipe': Recipe_List,
#                     'Most_Popular_Recipe': Most_Popular_Recipe_List}
#     return render(request, 'studenteats/recipe.html', context=context_dict)


def recipeHome(request):
    context_dict = {}
    context_dict['popular_recipes'] = Recipe.objects.order_by('-Likes')[0:6]
    if AdminDetails.objects.first() != None:
        context_dict['recipeWeek'] = AdminDetails.objects.first().recipeWeek
    context_dict['search'] = Recipe.objects.all()
    context_dict['link'] = "studeneats:show_recipes"
    return render(request, 'studenteats/recipeHome.html', context=context_dict)


def search_recipes(request):
    if request.method == "POST":
        if request.POST['searched'] != '':
            searched = request.POST['searched']
            recipes = Recipe.objects.filter(Q(Title__icontains=searched) |
                                            Q(Cuisine__icontains=searched) |
                                            Q(Tags__icontains=searched))
            context_dict = {}
            context_dict['searched'] = searched
            context_dict['recipes'] = list(recipes.all())
            return render(request, 'studenteats/search_recipes.html', context_dict)
    return recipeHome(request)


def show_recipes(request, Recipe_id):
    context_dict = {}
    recipe = Recipe.objects.filter(id=Recipe_id)[0]
    context_dict['recipe'] = recipe
    context_dict['count'] = Recipe.objects.filter(
        Owner__id=recipe.Owner.id).count()
    return render(request, 'studenteats/show_recipes.html', context=context_dict)


def forum(request, state=0):
    Discussion_like = Discussion.objects.order_by('-Likes')[:3]
    Discussion_view = Discussion.objects.order_by('-Views')[:3]
    Discussion_createdtime = Discussion.objects.order_by('-Created_Time')[:3]

    context_dict = {}

    if (state == 0):
        context_dict['Discussions'] = Discussion_like
    elif(state == 1):
        context_dict['Discussions'] = Discussion_view
    else:
        context_dict['Discussions'] = Discussion_createdtime

    return render(request, 'studenteats/forum.html', context=context_dict)


def discussion_detail(request, discussion_ID):

    discussion = Discussion.objects.filter(Discussion_ID=discussion_ID)
    reply = Discussion_Replies.objects.filter(Discussion_ID=discussion_ID)
    discussion = list(discussion)
    reply = list(reply)

    context_dict = {}
    context_dict = {'discussion': discussion, 'reply': reply}
    current_discussion = discussion[0].Discussion_ID
    request.session['diss_id'] = current_discussion  # 设置diss_id 存到session里

    print(context_dict)

    return render(request, 'studenteats/discussion_detail.html', context=context_dict)


def add_comments(request):
    diss_id = request.session.get('diss_id')
    user_id = request.user.id
    context_dict = {}
    context_dict = {'diss_id': diss_id, 'user_id': user_id}
    return render(request, 'studenteats/add_comments.html', context=context_dict)


def save_comments(request):
    if request.method == "POST":
        diss_id = request.session.get('diss_id')
        user_id = request.user.id
        rep_id = request.POST.get('rep_id')
        description = request.POST.get('description')
        create_time = DateField()
        likes = 0.0
        reply = Discussion_Replies(Description=description, User_ID=user_id,
                                   Created_Time=create_time, Likes=likes, Post_ID=rep_id, Discussion_ID=diss_id)

        return redirect(reverse('studenteats:forum'))
    else:
        return redirect(reverse('studenteats:forum'))


def help(request):
    context_dict = {}
    return render(request, 'studenteats/help.html', context=context_dict)


def getCoordinates(request, place):
    if not (Restaurant.objects.filter(Place__iexact=place).exists()):
        return JsonResponse({"valid": False}, status=200)
    return JsonResponse({"valid": True, "restaurants": list(Restaurant.objects.filter(Place__iexact=place).values('Latitude', 'Longitude', 'Name'))
                         }, status=200)


@login_required
def addRecipe(request):

    if(request.method == 'POST'):
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            cuisine = request.POST.get('cusine')
            check1 = request.POST.get('Value1')
            check2 = request.POST.get('Value2')
            check3 = request.POST.get('Value3')
            tags = {check1: "Easy", check2: "Quick", check3: "Advanced"}
            check = ""
            for k in tags.keys():
                if k != None:
                    check = tags[k]
            Owner = UserProfile.objects.filter(id=request.user.id)[0]
            r = Recipe.objects.create(Title=title, Content=content, Tags=check, Cuisine=cuisine, Owner=Owner)
            r.save()
            message = "true"
        except:
            message = "false"
        return render(request, 'studenteats/addRecipe.html', {'message': message, "add": "true", "id": request.user.id})

    else:
        return render(request, 'studenteats/addRecipe.html', {'id':request.user.id})

def deleteRecipe(request, id):
    Recipe.objects.filter(id=id).delete()
    return redirect('studenteats:profile', request.user.id)

def updateLikes(request, value, id):
    if(value == 1):
        Recipe.objects.filter(id=id).update(Likes=F('Likes')+1)
        return JsonResponse({"valid": True}, status=200)
    else:
        Recipe.objects.filter(id=id).update(Likes=F('Likes')-1)
        return JsonResponse({"valid": False}, status=200)
    
