# Generated by Django 4.1 on 2022-08-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.CharField(max_length=55),
        ),
    ]
