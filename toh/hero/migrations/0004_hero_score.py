
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