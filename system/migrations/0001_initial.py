# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=40, verbose_name='Event type')),
                ('item', models.CharField(max_length=40, verbose_name='Initiator')),
                ('description', models.CharField(max_length=80)),
                ('delta', models.PositiveIntegerField(verbose_name='Points change')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('defense', models.PositiveIntegerField(verbose_name='Defense PPR')),
                ('uptime', models.PositiveIntegerField(verbose_name='Uptime PPR')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('text', models.TextField(max_length=250, verbose_name='Description')),
                ('points', models.PositiveIntegerField(verbose_name='Points')),
                ('flag', models.CharField(max_length=32, verbose_name='Flag')),
            ],
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'task category',
                'verbose_name_plural': 'task categories',
            },
        ),
        migrations.CreateModel(
            name='TaskSolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solved_by', to='system.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Team name')),
                ('ip', models.CharField(default='0.0.0.0', max_length=15, verbose_name='Server IP')),
                ('pwd', models.CharField(default='.', max_length=20, verbose_name='SSH password')),
                ('invite', models.CharField(max_length=10, unique=True, verbose_name='Invite key')),
            ],
        ),
        migrations.CreateModel(
            name='TeamParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
                ('contact', models.TextField(max_length=400, verbose_name='Contact data')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='system.Team')),
            ],
            options={
                'verbose_name': 'participant',
            },
        ),
        migrations.AddField(
            model_name='tasksolution',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solved_tasks', to='system.Team'),
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='system.TaskCategory'),
        ),
        migrations.AddField(
            model_name='scoreevent',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='system.Team'),
        ),
    ]
