# Generated by Django 3.2.7 on 2021-09-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendees',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='attendees',
            name='attendees_phone',
            field=models.IntegerField(null=True),
        ),
    ]
