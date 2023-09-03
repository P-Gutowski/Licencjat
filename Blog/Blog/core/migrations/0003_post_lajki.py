# Generated by Django 4.2.4 on 2023-09-01 17:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_post_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lajki',
            field=models.ManyToManyField(related_name='posty', to=settings.AUTH_USER_MODEL),
        ),
    ]
