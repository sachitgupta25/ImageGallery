# Generated by Django 3.1.4 on 2021-01-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
