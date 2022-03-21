import os
from tokenize import Name
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iTECH_Group.settings')

import django
django.setup()
 
from studenteats.models import User,Recipe,Restaurant,Deals,Discussion,Discussion_Replies,Restaurant_Comments,Recipe_Comments, UserProfile

def populate():
    User_profiles = [

    {       'User_ID':1 ,
            'Name':'AliceA123',
            'Password':'123456',
            'Email': 'averagestudents@averagestudents.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""},

    {        'User_ID':2,
            'Name':'ironmansnap',
            'Password': '123456',
            'Email': 'ironmansnap@ironmansnap.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""},


    {       'User_ID':3,    
            'Name':'ghostfacegangsta',
            'Password': '123456',
            'Email': 'ghostfacegangsta@ghostfacegangsta.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':"" },


    {       'User_ID':4,    
            'Name':'MrsDracoMalfoy',
            'Password': '123456',
            'Email': 'MrsDracoMalfoy@MrsDracoMalfoy.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""},


    {       'User_ID':5,    
            'Name':'emilyramo',
            'Password': '123456',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Email': 'emilyramo@emilyramo.com',
            'Profile_Picture_Path':"" },


    {       'User_ID':6,
            'Name':'RidleyRich',
            'Password': '123456',
            'Email': 'RidleyRich@RidleyRich.com',
            'Location': 'Glasgow',
            'Role': 'Restaurant Owner',
            'Profile_Picture_Path':""},

    {
            'User_ID':7,
            'Name':'SuperMagnificentExtreme',
            'Password': '123456',
            'Location': 'Glasgow',
            'Role': 'Restaurant Owner',
            'Email': 'SuperMagnificentExtreme@SuperMagnificentExtreme.com',
            'Profile_Picture_Path':""}
    ]

    Recipes = [
        {
            'Recipe_ID':1, 
            'Title':'Jambalaya', 
            'Content': 'Step 1: Heat 1 tbsp olive oil in a large frying pan with a lid and brown 2 chopped chicken breasts for 5-8 mins until golden. STEP 2: Remove and set aside. Tip in the 1 diced onion and cook for 3-4 mins until soft. Step 3: Add 1 thinly sliced red pepper, 2 crushed garlic cloves, 75g sliced chorizo and 1 tbsp Cajun seasoning, and cook for 5 mins more. Step 4: Stir the chicken back in with 250g long grain rice, add the 400g can of tomatoes and 350ml chicken stock. Cover and simmer for 20-25 mins until the rice is tender.', 
            'Tags': 'Spicy, Chicken, Rice', 
            'Cuisine': 'Cajun', 
            'Created_Date': '2022-3-16', 
            'Owner': 2,
            'Likes':231,
        },

        {
            'Recipe_ID':2, 
            'Title':'Thai Green Curry', 
            'Content': 'Step 1: Put 225g new potatoes, cut into chunks, in a pan of boiling water and cook for 5 minutes. STEP 2: Add 100g trimmed and halved green beans and cook for a further 3 minutes, by which time both should be just tender but not too soft. Drain and put to one side. Step 3: In a wok or large frying pan, heat 1 tbsp vegetable or sunflower oil until very hot, then drop in 1 chopped garlic clove and cook until golden, this should take only a few seconds. Don’t let it go very dark or it will spoil the taste. Step 4: Spoon in 1 rounded tbsp Thai green curry paste and stir it around for a few seconds to begin to cook the spices and release all the flavours. Step 5: Next, pour in a 400ml can of coconut milk and let it come to a bubble. Step 6: Stir in 2 tsp Thai fish sauce and 1 tsp caster sugar, then 450g bite-size chicken pieces. Turn the heat down to a simmer and cook, covered, for about 8 minutes until the chicken is cooked. Step 6: Tip in the potatoes and beans and let them warm through in the hot coconut milk, then add 2 finely shredded lime leaves (or 3 wide strips lime zest). Step 7: Scatter with lime to garnish and serve immediately with boiled rice.', 
            'Tags': 'Thai, Chicken, Spicy', 
            'Cuisine': 'Thai', 
            'Created_Date': '2022-3-18', 
            'Owner': 3,
            'Likes':423,
        },

        {
            'Recipe_ID':3, 
            'Title':'Gnocchi', 
            'Content': 'Step 1: Cook the potatoes and lower them whole in their skins into a pan of salted boiling water, bring back to the boil and simmer for 10-15 minutes until just soft. Test with a sharp knife – you should have to push the knife in, it should not slide in easily, otherwise the potatoes will be overcooked and mushy and will have absorbed too much water. Peel them quickly, as the cooler they get, the less fluffy they become.Hold them in a tea towel to peel as they are hot. STEP 2: Using a mouli on a medium setting, press the potatoes into a bowl. Pass the potato through the mouli a second time, letting it fall on to the work surface. This second pressing is to make sure that the mixture is lump free, and also lets more air in. If you don’t have a mouli, you could use a potato ricer, but only if it has small holes, and you may need to push the potatoes through three times to get the right texture. Step 3: Make a hollow in your pile of potatoes, then pour in the egg and sprinkle over some of the flour. Start to blend everything with your hands, adding more flour but as little as you can get away with (you want the flavour of the potato to come through, rather than that of the flour).Work carefully and quickly, as the more you handle the dough, the harder and bouncier it will become. You need the same lightness you would use for pastry. Step 4:You should now have a soft dough that holds together, doesn’t feel sticky and can be easily shaped. Before you progress, check the dough by cooking a few gnocchi to see how they perform (see Valentina’s tip, right). Step 5: Divide the dough into 3 equal pieces. Roll a piece at a time into long, thumb-nail thick cylinders on a lightly floured surface, again working lightly and quickly. As you roll you will also be gently stretching the dough. Keep the surface well floured as you don’t want the gnocchi to stick. Step 6: Cut the dough into thumb-nail long lengths. Some people don’t bother to shape and pattern them, but just cook them as they are. However, the shaping and patterning gives a hollow on one side and a pattern on the other that enables the sauce to cling better, and also makes each piece recognisable as a gnocco (a single gnocchi). Step 7:Roll the gnocchi in a little flour. Holding them very lightly, form each into a small concave gnocchi shape: hold them against the prongs of the back of a fork, pressing only firmly enough to get the imprint (not so firmly that they go through the prongs), then guide each one so it tumbles away from the fork. Use your thumb as a guide and your fingers to pick and curl the gnocchi up. Spread them on a large board until required. Step 8: Boil', 
            'Tags': 'Italian, Potato, Comfort Food', 
            'Cuisine': 'Italian', 
            'Created_Date': '2022-3-17', 
            'Owner': 4,
            'Likes':296,
        },

        {
            'Recipe_ID':4, 
            'Title':'Simple Tasty Dressing', 
            'Content': 'Step 1: In a liquid measuring cup or bowl, combine oil, vinegar, mustard, honey, garlic, salt and pepper. Stir well with a small whisk or a fork until the ingredients are completely mixed together. Step 2: Taste, and adjust as necessary. If the mixture is too acidic, thin it out with a bit more olive oil or balance the flavors with a little more maple syrup or honey. If the mixture is a little blah, add another pinch or two of salt. If it doesn’t have enough zing, add vinegar by the teaspoon. Step 3: Serve immediately, or cover and refrigerate for future use. Homemade vinaigrette keeps well for 7 to 10 days. If your vinaigrette solidifies somewhat in the fridge, don’t worry about it—real olive oil tends to do that. Simply let it rest at room temperature for 5 to 10 minutes or microwave very briefly (about 20 seconds) to liquify the olive oil again. Whisk to blend and serve.', 
            'Tags': 'Dressing, Basics, Quick', 
            'Cuisine': 'Italian', 
            'Created_Date': '2022-3-7', 
            'Owner': 2,
            'Likes':123,
        }, 

        {   'Recipe_ID':5, 
            'Title':'Pizza Bagels', 
            'Content': 'Heat oven to 425°F. Spread 1 tablespoon pizza sauce over each bagel half. Sprinkle each with cheese and desired topping. Place on ungreased cookie sheet. Bake 5 to 10 minutes or until cheese is melted.',
            'Tags': 'Basics, Italian, Pizza', 
            'Cuisine': 'Italian', 
            'Created_Date': '2022-2-1', 
            'Owner': 1,
            'Likes':101,
        },

        {   'Recipe_ID':6, 
            'Title':'Cupcakes', 
            'Content': 'Using an electric whisk beat 110g softened butter and 110g golden caster sugar together until pale and fluffy then whisk in 2 large eggs, one at a time, scraping down the sides of the bowl after each addition. Add ½ tsp vanilla extract, 110g self-raising flour and a pinch of salt, whisk until just combined then spoon the mixture into the cupcake cases. Bake for 15 mins until golden brown and a skewer inserted into the middle of each cake comes out clean. Leave to cool completely on a wire rack.',
            'Tags': 'Dessert, Cake', 
            'Cuisine': 'Dessert', 
            'Created_Date': '2022-2-20', 
            'Owner': 5,
            'Likes':234,
        }

    ]

    Restaurants = [

        #deal is an interesting one. Is it a table we pass? passing 1 'main' deal for now

        {
            'Restaurant_ID':1,
            'Name':'Pizza Express',
            'Description': 'Mid range pizza chain with good deals',
            'Tags': 'Italian, Pizza, Mid-range',
            'Cuisine': 'Italian',
            'Owner': 6,
            'Res_Deals': 1,
            'Likes': 566,
            'Place':'Glasgow',
            'Latitude':55.8674822214843,
            'Longitude':-4.29110193068944
        },

        {
            'Restaurant_ID':2,
            'Name':'Shilling Brewing Co',
            'Description': 'Brew pub with student deals Sunday-Thursday',
            'Tags': 'Craft Beer, Pizza, Good for studying',
            'Cuisine': 'Italian',
            'Owner': 7,
            'Res_Deals': 2,
            'Likes': 498,
            'Place':'Glasgow',
            'Latitude':55.8597956805843,
            'Longitude':-4.25550460369966
        }, 

        {
            'Restaurant_ID':3,
            'Name':'Bar Soba',
            'Description': 'Asian fusion food and cocktails with student discount card',
            'Tags': 'Good Deals, Noodles, Multiple locations',
            'Cuisine': 'Asian Fusion',
            'Owner': 6,
            'Res_Deals': 3,
            'Likes': 388,
            'Place':'Glasgow',
            'Latitude':55.8620011014798,
            'Longitude':-4.2549319938944
        }, 

        {
            'Restaurant_ID':4,
            'Name':'Las Iguanas',
            'Description': 'Latin American restaurant and bar in the city centre',
            'Tags': 'Student discount, Bottomless Brunch, tapas',
            'Cuisine': 'Latin American',
            'Owner': 7,
            'Res_Deals': 4,
            'Likes': 226,
            'Place':'Edinburgh',
            'Latitude':55.9498107877072,
            'Longitude':-3.20705758412953
        }, 

        {
            'Restaurant_ID':5,
            'Name':'Yo Sushi',
            'Description': 'Sushi chain with rapid service',
            'Tags': 'Student discount, Sushi, Katsu',
            'Cuisine': 'Japanese',
            'Owner': 6,
            'Res_Deals': 3,
            'Likes': 643,
            'Place':'Edinburgh',
            'Latitude':55.93629914965932,
            'Longitude':-3.2413821536733685
        }, 

        {
            'Restaurant_ID':6,
            'Name':'Mother India',
            'Description': 'Award winning curry in a cosy setting',
            'Tags': 'Indian, Curry, Award-winning',
            'Cuisine': 'Indian',
            'Owner': 7,
            'Res_Deals': 4,
            'Likes': 845,
            'Place':'Edinburgh',
            'Latitude':55.95772009779098,
            'Longitude':-3.1336121670289505
        }, 
    ]

    Deals = [
        {
            'Deal_ID': 1,
            'Name': 'Buy One Get One Free',
            'Description': 'Buy one get one free Sunday to Thursday',
            'Last_Date': '2022-5-1'
        },

        {
            'Deal_ID': 2,
            'Name': '20% off for students',
            'Description': '20% off with a valid student card',
            'Last_Date': '2022-6-1'
        },

        {
            'Deal_ID': 3,
            'Name': '40% off for students',
            'Description': '40% off valid every day',
            'Last_Date': '2022-4-23'
        },

        {
            'Deal_ID': 4,
            'Name': '10% off',
            'Description': '10% off food only with a valid student card',
            'Last_Date': '2022-6-15'
        }
    ]

    Discussion_Posts = [
        {
            'Discussion_ID': 1,
            'Title': 'Where can I find this Sauce?',
            'Description': 'When I was on holiday in Malaysia last year I had these noodles with an amazing sauce and I can\'t find it or remember what it was called. It is like soy but sweeter and kinda ketchupy- help!' ,
            'Created_Time': '2022-1-23',
            'Owner': 1,
            'Views': 343,
            'Likes': 112
        },

        {   'Discussion_ID': 2,
            'Title': 'Did Ushas shut down?',
            'Description': 'I used to love the place but it looks like it changed or something. Anyone know what happened?' ,
            'Created_Time': '2022-2-8',
            'Owner': 2,
            'Views': 212,
            'Likes': 211
        }, 

        {
            'Discussion_ID': 3,
            'Title': 'Why is my egg always raw??!',
            'Description': 'I swear I am actually a good cook but every time I try to boil an egg it ends up totally raw in the middle. What is wrong with me??' ,
            'Created_Time': '2022-1-18',
            'Owner': 3,
            'Views':123,
            'Likes': 300
        },

        {
            'Discussion_ID': 4,
            'Title': 'Where is good to take my parents?',
            'Description': 'My parents are coming up from down south and they say they want to see Glasgow. I want to take them for some proper Scottish food but where would be good without breaking the bank?' ,
            'Created_Time': '2022-3-20',
            'Owner': 4,
            'Views': 112,
            'Likes': 200
        },

        {
            'Discussion_ID': 5,
            'Title': 'Not a question just a rant',
            'Description': 'EVERY TIME I TRY TO GET THE NOODLES I LIKE THEY NEVER HAVE THEM. WHAT IS WRONG WITH THIS CITY' ,
            'Created_Time': '2022-2-12',
            'Owner': 2,
            'Views': 335,
            'Likes': 321
        },

        {
            'Discussion_ID': 6,
            'Title': 'Homesick',
            'Description': 'I\'m an exchange student from Italy and I am so homesick right now. I can\'t afford flights home until Summer. Anyone else homesick and want to meet up and maybe share some recipes?' ,
            'Created_Time': '2022-3-17',
            'Owner': 1,
            'Views': 223,
            'Likes': 453
        }
    ]

    Replies = [
        {
            'Description': 'I think I saw it in the world food aisle in the big tesco in Maryhill',
            'Owner': 2,
            'Created_Time': '2022-1-24',
            'Likes': 98,
            'Post_ID':1,
            'Discussion_ID':1
        },
        {
            'Description': 'I know what you mean that stuff is great',
            'Owner': 3,
            'Created_Time': '2022-1-25',
            'Likes': 20,
            'Post_ID':2,
            'Discussion_ID':1
        },

        {
            'Description': 'Yeah it closed down during covid. Sad times',
            'Owner': 1,
            'Created_Time': '2022-1-23',
            'Likes': 31,
            'Post_ID':3,
            'Discussion_ID':2
        },

        {
            'Description': 'Yeah it closed down during covid. Sad times',
            'Owner': 1,
            'Created_Time': '2022-2-10',
            'Likes': 31,
            'Post_ID':4,
            'Discussion_ID':2
        },

        {
            'Description': 'I think there is a video on the recipe page you should look at',
            'Owner': 1,
            'Created_Time': '2022-2-10',
            'Likes': 60,
            'Post_ID':5,
            'Discussion_ID':3
        },

        {
            'Description': 'Cook for them! That is always cheapest...',
            'Owner': 4,
            'Created_Time': '2022-3-17',
            'Likes': 31,
            'Post_ID':6,
            'Discussion_ID':4
        },

        {
            'Description': 'I\'m from South Africa and I haven\'t been home in years. Let\'s definitely do something!',
            'Owner': 3,
            'Created_Time': '2022-2-10',
            'Likes': 31,
            'Post_ID':7,
            'Discussion_ID':6
        },

    ]

    Res_Comments = [

        {
            'Description': 'I love this place!',
            'Owner': 1,
            'Created_Time': '2022-2-21',
            'Likes': 32,
            'Comment_ID': 1,
            'Restaurant_ID': 1
        },

        {
            'Description': 'It\'s okay. Bit expensive though',
            'Owner': 2,
            'Created_Time': '2022-1-21',
            'Likes': 31,
            'Comment_ID': 2,
            'Restaurant_ID': 2
        },

        {
            'Description': 'It\'s dog friendly. I love it!',
            'Owner': 3,
            'Created_Time': '2022-3-12',
            'Likes': 87,
            'Comment_ID': 3,
            'Restaurant_ID': 3
        },

        {
            'Description': 'Staff are great. I sit and study there on quiet days',
            'Owner': 4,
            'Created_Time': '2022-1-11',
            'Likes': 64,
            'Comment_ID': 4,
            'Restaurant_ID': 5
        },

        {
            'Description': 'This place is sooooo good. Student discount is a bonus.',
            'Owner': 3,
            'Created_Time': '2022-3-10',
            'Likes': 64,
            'Comment_ID': 5,
            'Restaurant_ID': 6
        },
    ]

    Rec_Comments = [
        {
            'Description': 'OMG Delishious!',
            'Owner': 4,
            'Created_Time': '2022-3-10',
            'Likes': 12,
            'Comment_ID': 1,
            'Recipe_ID': 1
        },

        {
            'Description': 'I still can\'t get this right. Am I using the wrong kind of ingredients?',
            'Owner': 3,
            'Created_Time': '2022-3-11',
            'Likes': 22,
            'Comment_ID': 2,
            'Recipe_ID': 2
        },

        {
            'Description': 'So gooood. I never have time for this but it works!',
            'Owner': 1,
            'Created_Time': '2022-3-17',
            'Likes': 43,
            'Comment_ID': 3,
            'Recipe_ID': 3
        },

        {
            'Description': 'Simple but good. Everyone should have a look at this',
            'Owner': 2,
            'Created_Time': '2022-3-6',
            'Likes': 45,
            'Comment_ID': 4,
            'Recipe_ID': 4
        },

        {
            'Description': 'This is such good hangover food. Better than spending a fortune on Dominos',
            'Owner': 3,
            'Created_Time': '2022-3-12',
            'Likes': 98,
            'Comment_ID': 5,
            'Recipe_ID': 5
        },

        {
            'Description': 'Warm cupcakes is a game changer.',
            'Owner': 1,
            'Created_Time': '2022-2-22',
            'Likes': 231,
            'Comment_ID': 6,
            'Recipe_ID': 6
        }
    ]

    for user in User_profiles:
        u = add_User(user['User_ID'], user['Name'], user['Email'], user['Password'], user['Location'], user['Role'], user['Profile_Picture_Path'])
        print(f'{u}')

    for recipe in Recipes:
        r = add_Recipe(recipe['Recipe_ID'], recipe['Title'], recipe['Content'], recipe['Tags'], recipe['Cuisine'], recipe['Created_Date'], recipe['Owner'], recipe['Likes'])
        print(f'{r}')
        
    for deal in Deals:
        d = add_Deals(deal['Deal_ID'], deal['Name'], deal['Description'], deal['Last_Date'])
        print(f'{d}')
        
    for restaurant in Restaurants:
        res = add_Restaurant(restaurant['Restaurant_ID'],restaurant['Name'], restaurant['Description'], restaurant['Tags'], restaurant['Cuisine'], restaurant['Owner'], restaurant['Res_Deals'], restaurant['Likes'], restaurant['Latitude'], restaurant['Longitude'], restaurant['Place'])
        print(f'{res}')

    for discuss in Discussion_Posts:
        dis = add_Discussion(discuss['Discussion_ID'], discuss['Title'], discuss['Description'], discuss['Created_Time'], discuss['Owner'], discuss['Views'], discuss['Likes'])
        print(f'{dis}')

    for reply in Replies:
        rep = add_Discussion_Replies(reply['Description'],reply['Owner'],reply['Created_Time'],reply['Likes'],reply['Post_ID'],reply['Discussion_ID'])
        print(f'{rep}')

    for comment in Res_Comments:
        com = add_Restaurant_Comments(comment['Description'],comment['Owner'],comment['Created_Time'],comment['Likes'],comment['Comment_ID'],comment['Restaurant_ID'])
        print(f'{com}')

    for com in Rec_Comments:
        comment = add_Recipe_Comments(com['Description'],com['Owner'],com['Created_Time'],com['Likes'],com['Comment_ID'],com['Recipe_ID'])
        print(f'{comment}')


def add_User(User_ID,Name,Email,Password,Location,Role,Profile_Picture_Path):
    u=User.objects.create(username=User_ID)
    u.save()
    a = UserProfile.objects.get_or_create(user=u, name=Name,email=Email,password=Password,location=Location,role=Role,picture=Profile_Picture_Path)[0]
    a.save()
    return a

def add_Recipe(Recipe_ID,Title,Content,Tags,Cuisine,Created_Date,Owner,Likes):
    b = Recipe.objects.get_or_create(Recipe_ID=Recipe_ID, Title=Title, Content=Content, Tags=Tags, Cuisine=Cuisine, Created_Date=Created_Date, Owner=UserProfile.objects.get(id=Owner), Likes=Likes)[0]
    b.save()
    return b

def add_Restaurant(Restaurant_ID,Name,Description,Tags,Cuisine,Owner,Res_Deals,Likes,Latitude, Longitude, Place):
    c =Restaurant.objects.get_or_create(Restaurant_ID=Restaurant_ID,Name=Name,Description=Description,Tags=Tags,Cuisine=Cuisine,Owner=UserProfile.objects.get(id=Owner), Res_Deals=Deals.objects.get(Deal_ID=Res_Deals),Likes=Likes, Latitude=Latitude, Longitude=Longitude, Place=Place)[0]
    c.save()
    return c

def add_Deals(Deal_ID,Name,Description,Last_Date):
    d = Deals.objects.get_or_create(Deal_ID=Deal_ID,Name=Name,Description=Description,Last_Date=Last_Date)[0]
    d.save()
    return d

def add_Discussion(Discussion_ID,Title,Description,Created_Time,Owner,Views, Likes):
    e=Discussion.objects.get_or_create(Discussion_ID=Discussion_ID,Title=Title,Description=Description,Created_Time=Created_Time,User_ID=UserProfile.objects.get(id=Owner),Views=Views, Likes=Likes)[0]
    e.save()
    return e

def add_Discussion_Replies(Description,Owner,Created_Time,Likes,Post_ID,Discussion_ID):
    f = Discussion_Replies.objects.get_or_create(Description=Description,User_ID=UserProfile.objects.get(id=Owner),Created_Time=Created_Time,Likes=Likes,Post_ID=Post_ID,Discussion_ID=Discussion.objects.get(Discussion_ID=Discussion_ID))[0]
    f.save()
    return f

def add_Restaurant_Comments(Description,Owner,Created_Time,Likes,Comment_ID,Restaurant_ID):
    g=Restaurant_Comments.objects.get_or_create(Description=Description,User_ID=UserProfile.objects.get(id=Owner),Created_Time=Created_Time,Likes=Likes,Comment_ID=Comment_ID,Restaurant_ID=Restaurant.objects.get(Restaurant_ID=Restaurant_ID))[0]
    g.save()
    return g

def add_Recipe_Comments(Description,Owner,Created_Time,Likes,Comment_ID,Recipe_ID):
    h=Recipe_Comments.objects.get_or_create(Description=Description,User_ID=UserProfile.objects.get(id=Owner),Created_Time=Created_Time,Likes=Likes,Comment_ID=Comment_ID,Recipe_ID=Recipe.objects.get(id=Recipe_ID))[0]
    h.save()
    return h

if __name__=='__main__':
    print('Starting Rango population script...') 
    populate()