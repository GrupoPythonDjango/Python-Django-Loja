# Generated by Django 4.2 on 2023-05-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
    ]
