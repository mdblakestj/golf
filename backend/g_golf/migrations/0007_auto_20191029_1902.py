# Generated by Django 2.2.6 on 2019-10-29 19:02

from django.db import migrations, models
import django.db.models.deletion
import g_golf.models


class Migration(migrations.Migration):

    dependencies = [
        ('g_golf', '0006_delete_hats'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoleInst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_1_score', models.CharField(max_length=100)),
                ('player_2_score', models.CharField(max_length=100)),
                ('player_3_score', models.CharField(max_length=100)),
                ('player_4_score', models.CharField(max_length=100)),
            ],
            bases=(models.Model, g_golf.models.Base),
        ),
        migrations.RenameField(
            model_name='hole',
            old_name='long',
            new_name='lng',
        ),
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='course',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='course',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='game',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='game',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='hole',
            name='updated_at',
        ),
        migrations.DeleteModel(
            name='Hole_Inst',
        ),
        migrations.AddField(
            model_name='holeinst',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_golf.Game'),
        ),
        migrations.AddField(
            model_name='holeinst',
            name='hole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='g_golf.Hole'),
        ),
    ]
