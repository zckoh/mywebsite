# Generated by Django 2.2.7 on 2019-11-28 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191127_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
