# Generated by Django 4.1.5 on 2023-09-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_alter_uploadimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
