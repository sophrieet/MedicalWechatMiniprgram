# Generated by Django 2.2.10 on 2020-05-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0012_auto_20200507_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('doctor_id', models.CharField(default='', max_length=64, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]