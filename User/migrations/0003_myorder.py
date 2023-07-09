# Generated by Django 4.1.2 on 2022-12-07 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
        ('User', '0002_alter_account_house_alter_account_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.userinfo')),
            ],
            options={
                'db_table': 'Myorder',
            },
        ),
    ]