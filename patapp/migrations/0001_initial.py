# Generated by Django 3.0.5 on 2020-05-03 08:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('upload_key', models.CharField(default='', max_length=64, primary_key=True, serialize=False, unique=True)),
                ('upload_time', models.CharField(default='', max_length=64)),
                ('text', models.TextField(db_index=True, default='[]')),
                ('reply', models.TextField(default='[]')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('openid', models.CharField(default='', max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='openId')),
                ('session_key', models.CharField(max_length=256, verbose_name='session_key')),
                ('gender', models.CharField(default='', max_length=64, verbose_name='性别')),
                ('name', models.CharField(default='', max_length=64, verbose_name='语言')),
                ('mobile', models.CharField(max_length=32, verbose_name='小程序授权手机号')),
                ('age', models.CharField(default='', max_length=64, verbose_name='年龄')),
                ('first_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='imagereal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='', max_length=512, upload_to='D:\\workspace\\PythonProject\\djangotest\\static\\dbimg\\')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patapp.image')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patapp.user'),
        ),
    ]