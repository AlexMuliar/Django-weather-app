# Generated by Django 3.0.2 on 2020-01-30 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200130_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='tepm',
            field=models.FloatField(),
        ),
    ]
