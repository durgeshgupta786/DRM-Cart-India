# Generated by Django 3.2.15 on 2022-09-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_uregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uregister',
            name='userpic',
            field=models.ImageField(default='', upload_to='static/uregister/'),
        ),
    ]
