# Generated by Django 2.1.5 on 2022-03-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenteats', '0007_auto_20220317_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion_replies',
            name='Discussion_ID',
            field=models.IntegerField(default=0),
        ),
    ]
