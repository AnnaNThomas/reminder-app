# Generated by Django 4.0.4 on 2022-06-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0010_alter_dt_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dt',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
