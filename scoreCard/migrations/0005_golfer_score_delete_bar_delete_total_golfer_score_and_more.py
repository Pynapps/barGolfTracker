# Generated by Django 4.2.4 on 2023-08-05 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scoreCard', '0004_alter_total_total_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Golfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('do_dodge', models.IntegerField(default=0)),
                ('wigwam', models.IntegerField(default=0)),
                ('depot', models.IntegerField(default=0)),
                ('sports_page', models.IntegerField(default=0)),
                ('reboot', models.IntegerField(default=0)),
                ('mouse_trap', models.IntegerField(default=0)),
                ('clancys', models.IntegerField(default=0)),
                ('dooleys', models.IntegerField(default=0)),
                ('gi', models.IntegerField(default=0)),
                ('brothers', models.IntegerField(default=0)),
                ('pio', models.IntegerField(default=0)),
                ('pickle', models.IntegerField(default=0)),
                ('shenanns', models.IntegerField(default=0)),
                ('brat', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Bar',
        ),
        migrations.DeleteModel(
            name='Total',
        ),
        migrations.AddField(
            model_name='golfer',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoreCard.score'),
        ),
        migrations.AddField(
            model_name='golfer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
