# Generated by Django 2.0.2 on 2018-03-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('okr', '0009_auto_20180307_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='globalkeyresult',
            old_name='complete_percentage',
            new_name='percentage',
        ),
        migrations.RenameField(
            model_name='objective',
            old_name='complete_percentage',
            new_name='percentage',
        ),
        migrations.RemoveField(
            model_name='globalkeyresult',
            name='incomplete_percentage',
        ),
        migrations.RemoveField(
            model_name='globalkeyresult',
            name='null_percentage',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='incomplete_percentage',
        ),
        migrations.RemoveField(
            model_name='objective',
            name='null_percentage',
        ),
        migrations.AlterField(
            model_name='result',
            name='manual_bar',
            field=models.BooleanField(default=False, help_text=' If you select this, DO NOT select any jira_issues.',
                                      verbose_name='Manual Progress Bar'),
        ),
    ]
