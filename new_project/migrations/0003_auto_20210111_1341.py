# Generated by Django 3.1.4 on 2021-01-11 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0002_image_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]