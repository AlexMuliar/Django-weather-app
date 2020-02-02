# Generated by Django 3.0.2 on 2020-01-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200130_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='icon',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='tepm',
            field=models.FloatField(default=None),
        ),
    ]
