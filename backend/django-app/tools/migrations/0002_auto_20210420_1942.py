# Generated by Django 3.2 on 2021-04-20 17:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bratool', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalTools',
            new_name='HistoricalTool',
        ),
        migrations.RenameModel(
            old_name='Tools',
            new_name='Tool',
        ),
        migrations.AlterModelOptions(
            name='historicaltool',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical tool'},
        ),
    ]
