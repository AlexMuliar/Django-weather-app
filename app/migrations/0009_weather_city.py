# Generated by Django 3.0.2 on 2020-01-30 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200130_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.City'),
        ),
    ]
