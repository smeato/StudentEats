# Generated by Django 2.1.5 on 2022-03-16 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studenteats', '0010_auto_20220316_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='User_ID',
            new_name='Owner',
        ),
    ]
