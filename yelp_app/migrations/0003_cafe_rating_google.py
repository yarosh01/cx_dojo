# Generated by Django 3.2.9 on 2021-11-24 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_app', '0002_auto_20211124_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='rating_google',
            field=models.CharField(max_length=250, null=True),
        ),
    ]