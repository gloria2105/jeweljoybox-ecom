# Generated by Django 4.2.5 on 2024-07-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart_rename_ame_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
