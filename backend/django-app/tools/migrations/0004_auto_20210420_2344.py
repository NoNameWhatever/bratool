# Generated by Django 3.2 on 2021-04-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bratool', '0002_auto_20210420_2329'),
        ('tools', '0003_auto_20210420_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalgenre',
            name='departments',
        ),
        migrations.RemoveField(
            model_name='historicaltool',
            name='department',
        ),
        migrations.RemoveField(
            model_name='historicaltool',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='departments',
        ),
        migrations.AddField(
            model_name='genre',
            name='departments',
            field=models.ManyToManyField(blank=True, null=True, to='bratool.Department', verbose_name='department'),
        ),
        migrations.RemoveField(
            model_name='tool',
            name='department',
        ),
        migrations.AddField(
            model_name='tool',
            name='department',
            field=models.ManyToManyField(null=True, to='bratool.Department', verbose_name='department'),
        ),
        migrations.RemoveField(
            model_name='tool',
            name='genre',
        ),
        migrations.AddField(
            model_name='tool',
            name='genre',
            field=models.ManyToManyField(null=True, to='tools.Genre', verbose_name='genre'),
        ),
    ]
