# Generated by Django 3.2.7 on 2021-09-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
