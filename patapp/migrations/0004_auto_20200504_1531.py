# Generated by Django 3.0.5 on 2020-05-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0003_auto_20200504_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagereal',
            name='img',
            field=models.ImageField(default='', max_length=512, upload_to='\\images'),
        ),
    ]