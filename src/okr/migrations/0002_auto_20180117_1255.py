# Generated by Django 2.0.1 on 2018-01-17 12:55

from decimal import Decimal

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('okr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('Modified Objective', 'Modified Objective'),
                                                   ('Modified Key Result', 'Modified Key Result'),
                                                   ('Deleted Objective', 'Deleted Objective'),
                                                   ('Deleted Key Result', 'Deleted Key Result'),
                                                   ('Created Objective', 'Created Objective'),
                                                   ('Created Key Result', 'Created Key Result'),
                                                   ('Completed Objective', 'Completed Objective'),
                                                   ('Completed Key Result', 'Completed Key Result')], max_length=100)),
                ('data', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalKeyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('key_result', models.TextField()),
            ],
            options={
                'verbose_name': 'Global Key Result',
                'verbose_name_plural': 'Global Key Results',
            },
        ),
        migrations.CreateModel(
            name='GlobalObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('objective', models.TextField(help_text='This is the overall objective eg. Be ITRIC Compliant.')),
            ],
            options={
                'verbose_name': 'Global Objective',
                'verbose_name_plural': 'Global Objectives',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=50)),
                ('priority', models.CharField(
                    choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Mandatory', 'Mandatory')],
                    default='Low', max_length=10)),
                ('status', models.BooleanField(default=False)),
                ('summary', models.TextField(blank=True)),
                ('type', models.CharField(
                    choices=[('Task', 'Task'), ('Sub-Task', 'Sub-Task'), ('Story', 'Story'), ('Incident', 'Incident')],
                    default='Task', max_length=20)),
                ('story_points', models.IntegerField(default=0)),
                ('coin_value', models.IntegerField(default=0)),
                ('tmp_status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                           related_name='user_issue_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('objective', models.TextField(help_text='This is your objective you would like to submit.')),
                ('percentage', models.FloatField(default=0)),
                ('global_key_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='okr',
                                                        to='okr.GlobalKeyResult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objective_set',
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Objective',
                'verbose_name_plural': 'User Objectives',
            },
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Quarter',
                'verbose_name_plural': 'Quarters',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('result', models.TextField(help_text='This is your key result related to your objective.')),
                ('manual_bar', models.BooleanField(default=False)),
                ('percentage', models.FloatField(default=0)),
                ('jira_issues', models.ManyToManyField(blank=True, to='okr.Issue')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okr.Objective')),
            ],
            options={
                'verbose_name': 'User Key Result',
                'verbose_name_plural': 'User Key Results',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='energy',
            field=models.DecimalField(decimal_places=0, default=Decimal('100.0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='gems',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='karma',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='xp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='globalobjective',
            name='quarter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okr.Quarter'),
        ),
        migrations.AddField(
            model_name='globalkeyresult',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okr.GlobalObjective'),
        ),
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='team_user_set', to='okr.Team'),
        ),
    ]
