# Generated by Django 4.1.2 on 2022-10-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
