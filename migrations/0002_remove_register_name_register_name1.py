# Generated by Django 4.0.4 on 2022-05-26 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='name',
        ),
        migrations.AddField(
            model_name='register',
            name='name1',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
