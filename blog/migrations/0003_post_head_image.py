# Generated by Django 3.2.15 on 2022-10-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20221006_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='blog/images/%Y/%m/%d/'),
        ),
    ]
