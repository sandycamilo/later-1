# Generated by Django 2.2.7 on 2020-04-12 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0007_auto_20200404_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.CharField(default='http://placehold.it/700x400', max_length=200),
        ),
    ]
