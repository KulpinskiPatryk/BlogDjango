# Generated by Django 4.0.3 on 2022-04-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/mk.png', upload_to='images/'),
        ),
    ]
