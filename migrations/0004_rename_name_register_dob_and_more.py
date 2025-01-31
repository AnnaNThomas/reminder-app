# Generated by Django 4.0.4 on 2022-05-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_rename_name1_register_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='name',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='phone',
            new_name='mobile',
        ),
        migrations.AddField(
            model_name='register',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
