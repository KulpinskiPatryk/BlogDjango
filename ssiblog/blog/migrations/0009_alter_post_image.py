# Generated by Django 4.0.3 on 2022-04-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='images/%Y/%m/%d/'),
        ),
    ]
