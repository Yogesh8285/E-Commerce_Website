# Generated by Django 4.1.2 on 2022-12-06 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='PaymentMaster',
            fields=[
                ('cardno', models.IntegerField(max_length=16, primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(max_length=3)),
                ('expiry', models.CharField(max_length=20)),
                ('ballance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'PaymentMaster',
            },
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='abc.jpg', upload_to='Images')),
            ],
            options={
                'db_table': 'Recent_Update',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('price', models.FloatField(default=200)),
                ('description', models.CharField(max_length=50)),
                ('size', models.FloatField(default=1)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(default='abc.jpg', upload_to='Images')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.category')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
