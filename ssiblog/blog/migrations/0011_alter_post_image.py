# Generated by Django 4.0.3 on 2022-04-18 10:34

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_dateofcreated_remove_post_dateofupdated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/mk.png', upload_to='images/'),
        ),
    ]