# Generated by Django 5.0.2 on 2024-03-04 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_options_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['user']},
        ),
    ]
