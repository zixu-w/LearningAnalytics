# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrolledCourse',
        ),
        migrations.AddField(
            model_name='student',
            name='enrolledCourse',
            field=models.ManyToManyField(to='presentation.Course'),
        ),
    ]
