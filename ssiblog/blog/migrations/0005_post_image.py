# Generated by Django 4.0.3 on 2022-04-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images/%Y/%m/%d/'),
        ),
    ]
