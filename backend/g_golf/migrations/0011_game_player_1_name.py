# Generated by Django 2.2.6 on 2019-11-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_golf', '0010_auto_20191029_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player_1_name',
            field=models.CharField(default='Dan', max_length=100),
            preserve_default=False,
        ),
    ]
