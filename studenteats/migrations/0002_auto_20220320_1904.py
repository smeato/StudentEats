# Generated by Django 2.1.5 on 2022-03-20 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('studenteats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('telephone', models.CharField(blank=True, max_length=50, verbose_name='Telephone')),
                ('birthday', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('email', models.TextField(max_length=1000)),
                ('university', models.CharField(blank=True, max_length=50, verbose_name='university')),
                ('password', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='location')),
                ('role', models.CharField(max_length=20)),
                ('picture', models.ImageField(blank=True, upload_to='profile_image')),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='discussion',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.AlterField(
            model_name='discussion_replies',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.AlterField(
            model_name='recipe_comments',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='Owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.AlterField(
            model_name='restaurant_comments',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studenteats.UserProfile'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
