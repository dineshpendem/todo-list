# Generated by Django 5.0.2 on 2024-03-04 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]
