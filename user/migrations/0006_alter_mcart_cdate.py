# Generated by Django 3.2.15 on 2022-09-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_uregister_passwd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcart',
            name='cdate',
            field=models.CharField(max_length=100),
        ),
    ]
