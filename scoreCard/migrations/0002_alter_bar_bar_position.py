# Generated by Django 4.2.4 on 2023-08-04 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreCard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='bar_position',
            field=models.IntegerField(),
        ),
    ]
