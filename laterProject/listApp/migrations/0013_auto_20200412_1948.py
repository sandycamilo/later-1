# Generated by Django 2.2.7 on 2020-04-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listApp', '0012_auto_20200412_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(),
        ),
    ]