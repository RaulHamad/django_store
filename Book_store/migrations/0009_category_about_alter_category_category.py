# Generated by Django 5.0.3 on 2024-04-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_store', '0008_category_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
