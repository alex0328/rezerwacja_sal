# Generated by Django 2.1.4 on 2018-12-17 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezervation', '0002_auto_20181217_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]