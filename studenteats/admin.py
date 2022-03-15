from django.contrib import admin
from studenteats.models import UserProfile
from studenteats.models import User, Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Restaurant)
admin.site.register(Deals)
admin.site.register(Discussion)
admin.site.register(Discussion_Replies)
admin.site.register(Restaurant_Comments)
admin.site.register(Recipe_Comments)
