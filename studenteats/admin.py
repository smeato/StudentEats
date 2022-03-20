from django.contrib import admin
from studenteats.models import UserProfile
from studenteats.models import AdminDetails, User, Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Deals)
admin.site.register(Restaurant)
admin.site.register(Discussion)
admin.site.register(Discussion_Replies)
admin.site.register(Restaurant_Comments)
admin.site.register(Recipe_Comments)
admin.site.register(AdminDetails)

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model=UserProfile
    
class UserProfileAdmin(UserAdmin):
    inlines=[UserProfileInline,]

admin.site.register(User,UserProfileAdmin)
