# Generated by Django 2.2.6 on 2019-10-27 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('g_golf', '0003_auto_20191026_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='hole_1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_10',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_11',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_12',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_13',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_14',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_15',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_16',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_17',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_18',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_2',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_3',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_4',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_5',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_6',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_7',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_8',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hole_9',
        ),
        migrations.CreateModel(
            name='CourseHole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='g_golf.Course')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='g_golf.Hole')),
            ],
        ),
    ]
