# Generated by Django 4.2.1 on 2023-06-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundo1real', '0002_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.IntegerField(max_length=100),
        ),
    ]