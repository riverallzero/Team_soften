# Generated by Django 3.2.15 on 2022-12-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20221217_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='notice/images/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]