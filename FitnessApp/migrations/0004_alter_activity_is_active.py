# Generated by Django 3.2.25 on 2024-12-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FitnessApp', '0003_alter_activity_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='is_active',
            field=models.IntegerField(default='1'),
        ),
    ]
