# Generated by Django 2.1.5 on 2022-03-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deal_ID', models.IntegerField(default=0, unique=True)),
                ('Name', models.CharField(max_length=128)),
                ('Discount', models.FloatField(default=0)),
                ('Original_Price', models.FloatField(default=0)),
                ('Description', models.TextField(max_length=1000)),
                ('Last_Date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Deals',
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discussion_ID', models.IntegerField(default=0)),
                ('Title', models.CharField(max_length=128)),
                ('Description', models.TextField(max_length=1000)),
                ('Created_Time', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discussion_Replies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=1000)),
                ('Created_Time', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
                ('Post_ID', models.IntegerField(default=0, unique=True)),
                ('Discussion_ID', models.IntegerField(default=0, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Discussion replies',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_ID', models.IntegerField(default=0, unique=True)),
                ('Title', models.CharField(max_length=128)),
                ('Content', models.TextField(blank=True, max_length=1000)),
                ('Tags', models.CharField(max_length=128, null=True)),
                ('Cuisine', models.CharField(max_length=20)),
                ('Created_Date', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=1000)),
                ('Created_Time', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
                ('Comment_ID', models.IntegerField(default=0, unique=True)),
                ('Recipe_ID', models.ForeignKey(on_delete='cascade', to='studenteats.Recipe')),
            ],
            options={
                'verbose_name_plural': 'Recipe comments',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_ID', models.IntegerField(default=0, unique=True)),
                ('Name', models.CharField(max_length=10)),
                ('Description', models.TextField(max_length=1000)),
                ('Tags', models.CharField(max_length=128)),
                ('Cuisine', models.CharField(max_length=20)),
                ('Deals', models.TextField(max_length=200)),
                ('Likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(max_length=1000)),
                ('Created_Time', models.DateTimeField()),
                ('Likes', models.IntegerField(default=0)),
                ('Comment_ID', models.IntegerField(default=0, unique=True)),
                ('Restaurant_ID', models.ForeignKey(on_delete='cascade', to='studenteats.Restaurant')),
            ],
            options={
                'verbose_name_plural': 'Restaurant comments',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.IntegerField(default=0, unique=True)),
                ('Name', models.CharField(max_length=128)),
                ('Email', models.TextField(max_length=1000)),
                ('Password', models.CharField(max_length=200)),
                ('Location', models.TextField(max_length=200)),
                ('Role', models.CharField(max_length=20)),
                ('Prfoile_Picture_Path', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
        migrations.AddField(
            model_name='restaurant_comments',
            name='User_ID',
            field=models.ForeignKey(on_delete='cascade', to='studenteats.User'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.User'),
        ),
        migrations.AddField(
            model_name='recipe_comments',
            name='User_ID',
            field=models.ForeignKey(on_delete='cascade', to='studenteats.User'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.User'),
        ),
        migrations.AddField(
            model_name='discussion_replies',
            name='User_ID',
            field=models.ForeignKey(on_delete='cascade', to='studenteats.User'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.User'),
        ),
    ]
