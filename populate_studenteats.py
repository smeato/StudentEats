import os
from tokenize import Name

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iTECH_Group.settings')

import django
django.setup()
 
from studenteats.models import User,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments

def populate():
    users= {

        'averagestudents':{'ID':1,
                            'Name':'averagestudents',
                            'Password':'123456',
                            'Email': 'averagestudents@averagestudents.com',
                            'Location': 'Glasgow',
                            'Role': 'Student',
                            'Profile_Picture_Path':"",},

        # 'ironmansnap':{ 'ID':2,
        #                 'Name':'ironmansnap',
        #                 'Password': '123456',
        #                 'Email': 'ironmansnap@ironmansnap.com',
        #                 'Location': 'Glasgow',
        #                 'Role': 'Student',
        #                 'Profile_Picture_Path':"",
        #                 },

        # 'ghostfacegangsta':{'ID':3,    
        #                     'Name':'ghostfacegangsta',
        #                     'Password': '123456',
        #                     'Email': 'ghostfacegangsta@ghostfacegangsta.com',
        #                     'Location': 'Glasgow',
        #                     'Role': 'Student',
        #                     'Profile_Picture_Path':"",
        #                     },

        # 'MrsDracoMalfoy':{  'ID':4,    
        #                     'Name':'MrsDracoMalfoy',
        #                     'Password': '123456',
        #                     'Email': 'MrsDracoMalfoy@MrsDracoMalfoy.com',
        #                     'Location': 'Glasgow',
        #                     'Role': 'Student',
        #                     'Profile_Picture_Path':"",
        #                     },

        # 'emilyramo':{   'ID':5,    
        #                 'Name':'emilyramo',
        #                 'Password': '123456',
        #                 'Location': 'Glasgow',
        #                 'Role': 'Student',
        #                 'Email': 'emilyramo@emilyramo.com',
        #                 'Profile_Picture_Path':"",
        #                 },

        # 'RidleyRich':{'ID':6,
        #             'Name':'RidleyRich',
        #             'Password': '123456',
        #             'Email': 'RidleyRich@RidleyRich.com',
        #             'Location': 'Glasgow',
        #             'Role': 'Student',
        #             'Profile_Picture_Path':"",},

        # 'SuperMagnificentExtreme':{
        #                             'ID':7,
        #                             'Name':'SuperMagnificentExtreme',
        #                             'Password': '123456',
        #                             'Location': 'Glasgow',
        #                             'Role': 'Student',
        #                             'Email': 'SuperMagnificentExtreme@SuperMagnificentExtreme.com',
        #                             'Profile_Picture_Path':""
        #                             }
        }


    for username,data in users.items():
        add_User(data['ID'],username,data['Email'],data['Password'],data['Location'],data['Role'],data['Profile_Picture_Path'])



def add_User(User_ID,Name,Email,Password,Location,Role,Profile_Picture_Path):
    a = User(User_ID=User_ID, Name=Name, Email=Email,Password=Password,Location=Location,Role=Role,Profile_Picture_Path=Profile_Picture_Path)
    a.save()
    return a

def add_Recipe(Recipe_ID,Title,Content,Tags,Cuisine,Created_Date,User_ID,Likes):
    b = Recipe.objects
    b.Recipe_ID=Recipe_ID
    b.Title=Title,
    b.Content=Content,
    b.Tags=Tags,
    b.Cuisine=Cuisine,
    b.Created_Date=Created_Date,
    b.User_ID=User_ID,
    b.Likes=Likes
    b.save()
    return b

def add_Restaurant(Restaurant_ID,Name,Description,Tags,Cuisine,Owner,Deals,Likes):
    c =Restaurant.objects
    c.Restaurant_ID=Restaurant_ID
    c.Name=Name
    c.Description=Description
    c.Tags=Tags
    c.Cuisine=Cuisine
    c.Owner=Owner
    c.Deals=Deals
    c.Likes=Likes
    return c

def add_Deals(Deal_ID,Name,Discount,Original_Price,Description,Last_Date):
    d = Deals.objects
    d.Deal_ID=Deal_ID
    d.Name=Name
    d.Discount=Discount
    d.Original_Price=Original_Price
    d.Description=Description
    d.Last_Date=Last_Date
    return d

def add_Discussion(Discussion_ID,Title,Description,Created_Time,User_ID,Likes):
    e=Discussion.objects
    e.Discussion_ID=Discussion_ID
    e.Title=Title
    e.Description=Description
    e.Created_Time=Created_Time
    e.User_ID=User_ID
    e.Likes=Likes
    return e

def add_Discussion_Replies(Description,User_ID,Created_Time,Likes,Post_ID,Discussion_ID):
    f=Discussion_Replies.objects
    f.Description=Description
    f.User_ID=User_ID
    f.Created_Time=Created_Time
    f.Likes=Likes
    f.Post_ID=Post_ID
    f.Discussion_ID=Discussion_ID
    return f

def add_Restaurant_Comments(Description,User_ID,Created_Time,Likes,Comment_ID,Restaurant_ID):
    g=Restaurant_Comments.objects
    g.Description=Description
    g.User_ID=User_ID
    g.Created_Time=Created_Time
    g.Likes=Likes
    g.Comment_ID=Comment_ID
    g.Restaurant_ID=Restaurant_ID
    return g

def add_Recipe_Comments(Description,User_ID,Created_Time,Likes,Comment_ID,Recipe_ID):
    h=Recipe_Comments.objects
    h.Description=Description
    h.User_ID=User_ID
    h.Created_Time=Created_Time
    h.Likes=Likes
    h.Comment_ID=Comment_ID
    h.Recipe_ID=Recipe_ID
    return h

if __name__=='__main__':
    print('Starting Rango population script...') 
    populate()