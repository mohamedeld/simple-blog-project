# Generated by Django 3.2.6 on 2021-08-30 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_app', '0002_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
