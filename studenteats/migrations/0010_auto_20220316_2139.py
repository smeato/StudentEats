# Generated by Django 2.1.5 on 2022-03-16 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studenteats', '0009_auto_20220316_2127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Owner',
            new_name='User_ID',
        ),
    ]
