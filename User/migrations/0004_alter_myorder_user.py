# Generated by Django 4.1.2 on 2022-12-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_myorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='user',
            field=models.CharField(max_length=20),
        ),
    ]
