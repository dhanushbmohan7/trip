# Generated by Django 3.0.8 on 2020-12-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20201222_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='tableclass',
            field=models.CharField(default='table-active', max_length=10),
        ),
    ]
