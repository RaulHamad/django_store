# Generated by Django 5.0.3 on 2024-03-24 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_store', '0003_alter_book_download_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/%Y/%m/%d'),
        ),
    ]