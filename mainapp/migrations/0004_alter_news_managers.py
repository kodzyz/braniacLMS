# Generated by Django 4.0.4 on 2022-05-26 22:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_course_lesson_coursesteachers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
