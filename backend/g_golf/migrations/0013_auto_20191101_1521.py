# Generated by Django 2.2.6 on 2019-11-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_golf', '0012_auto_20191101_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_2_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_3_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_4_name',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
