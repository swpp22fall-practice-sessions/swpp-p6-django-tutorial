# Generated by Django 3.2.15 on 2022-10-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='age',
            field=models.IntegerField(default=25),
        ),
    ]
