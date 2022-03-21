from django.urls import reverse, resolve
from django.test import TestCase

from studenteats import views, models

####### Testing the urls #######
    
# 1. Test to check if the urls are working

class Tests(TestCase):
    urls = ['restaurant/', 'recipe/', 'help/', 'forum/', 'login/', 'add-recipe/']   
    reverseUrls = {'login': views.user_login, 'recipe':views.recipeHome, 'restaurant':views.restaurant, 'forum':views.forum, 'about':views.about, 'add-recipe':views.addRecipe}
    user_entry = {
             'User_ID':2,
            'Name':'ironmansnap',
            'Password': '123456',
            'Email': 'ironmansnap@ironmansnap.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""
        }
    recipe_entry = {
        'Recipe_ID':100, 
        'Title':'Jambalaya', 
        'Content': 'Step 1: Heat 1 tbsp olive oil in a large frying pan with a lid and brown 2 chopped chicken breasts for 5-8 mins until golden. STEP 2: Remove and set aside. Tip in the 1 diced onion and cook for 3-4 mins until soft. Step 3: Add 1 thinly sliced red pepper, 2 crushed garlic cloves, 75g sliced chorizo and 1 tbsp Cajun seasoning, and cook for 5 mins more. Step 4: Stir the chicken back in with 250g long grain rice, add the 400g can of tomatoes and 350ml chicken stock. Cover and simmer for 20-25 mins until the rice is tender.', 
        'Tags': 'Spicy, Chicken, Rice', 
        'Cuisine': 'Cajun', 
        'Created_Date': '2022-3-16', 
        'Owner': 2,
        'Likes':231,
    }
 

    # To test if the main page urls in the application works
    def testAppPages(self):
        for url in self.urls:
            response = self.client.get('/studenteats/'+url, follow=True)
            print(url, " ", response.status_code)
            self.assertEqual(response.status_code, 200)
        print("###################################################")

    # To test if the main page relative urls work
    def testReverseUrls(self):
        for k in self.reverseUrls.keys():
            url = reverse("studenteats:"+k)
            print("Resolve: ", resolve(url))
            self.assertEquals(resolve(url).func, self.reverseUrls[k])
        print("###################################################")


# 2. Test if the creating and deleting a User, Recipe work

    # Test for Recipe
    def testCreateDeleteRecipe(self):
        user_entry = {
             'User_ID':2,
            'Name':'ironmansnap',
            'Password': '123456',
            'Email': 'ironmansnap@ironmansnap.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""
        }
        recipe_entry = {
            'Recipe_ID':100, 
            'Title':'Jambalaya', 
            'Content': 'Step 1: Heat 1 tbsp olive oil in a large frying pan with a lid and brown 2 chopped chicken breasts for 5-8 mins until golden. STEP 2: Remove and set aside. Tip in the 1 diced onion and cook for 3-4 mins until soft. Step 3: Add 1 thinly sliced red pepper, 2 crushed garlic cloves, 75g sliced chorizo and 1 tbsp Cajun seasoning, and cook for 5 mins more. Step 4: Stir the chicken back in with 250g long grain rice, add the 400g can of tomatoes and 350ml chicken stock. Cover and simmer for 20-25 mins until the rice is tender.', 
            'Tags': 'Spicy, Chicken, Rice', 
            'Cuisine': 'Cajun', 
            'Created_Date': '2022-3-16', 
            'Owner': 2,
            'Likes':231,
        }
        user = models.User.objects.create(username=10000)
        Owner = models.UserProfile.objects.get_or_create(user=user, name=user_entry['Name'],email=user_entry['Email'],password=user_entry['Password'],location=user_entry['Location'],role=user_entry['Role'],picture=user_entry['Profile_Picture_Path'])[0]
        recipe = models.Recipe.objects.get_or_create(Recipe_ID=recipe_entry['Recipe_ID'], Title=recipe_entry['Title'], Content=recipe_entry['Content'], Tags=recipe_entry['Tags'], Cuisine=recipe_entry['Cuisine'], Created_Date=recipe_entry['Created_Date'], Owner=Owner, Likes=recipe_entry['Likes'])[0]
        self.assertEquals(recipe.Title, recipe_entry['Title'])
        self.assertEquals(recipe.Likes, recipe_entry['Likes'])
        self.assertEquals(recipe.Owner.name,'ironmansnap' )
        self.assertEquals(recipe.Tags, recipe_entry['Tags'])
        self.assertEquals(recipe.Cuisine, recipe_entry['Cuisine'])
        self.assertEquals(recipe.Created_Date, recipe_entry['Created_Date'])
        print("###################################################")


# 3. Test if editing the user information works

    def testEditUser(self):
        user_entry = {
             'User_ID':2,
            'Name':'ironmansnap',
            'Password': '123456',
            'Email': 'ironmansnap@ironmansnap.com',
            'Location': 'Glasgow',
            'Role': 'Student',
            'Profile_Picture_Path':""
        }
        user = models.User.objects.create(username=10000)
        Owner = models.UserProfile.objects.get_or_create(user=user, name=user_entry['Name'],email=user_entry['Email'],password=user_entry['Password'],location=user_entry['Location'],role=self.user_entry['Role'],picture=user_entry['Profile_Picture_Path'])[0]
        Owner.save()
        readOwner = models.UserProfile.objects.get(id=Owner.id)
        readOwner.name="new name"
        readOwner.save()
        readAgainOwner = models.UserProfile.objects.get(id=Owner.id)
        self.assertEquals(readAgainOwner.name, "new name")

        


     
