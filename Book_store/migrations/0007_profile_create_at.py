# Generated by Django 5.0.3 on 2024-03-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_store', '0006_rename_user_shopping_user_id_shopping_date_buy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
    ]