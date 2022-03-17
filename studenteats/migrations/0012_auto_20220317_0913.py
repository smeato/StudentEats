# Generated by Django 2.1.5 on 2022-03-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studenteats', '0011_auto_20220316_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deals',
            name='Discount',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='Original_Price',
        ),
        migrations.RemoveField(
            model_name='deals',
            name='id',
        ),
        migrations.AddField(
            model_name='deals',
            name='Deal_ID',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
        ),
    ]
