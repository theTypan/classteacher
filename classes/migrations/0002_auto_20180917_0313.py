# Generated by Django 2.1.1 on 2018-09-17 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
