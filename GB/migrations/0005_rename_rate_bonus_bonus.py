# Generated by Django 4.2.6 on 2023-10-31 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GB', '0004_bonus_passager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bonus',
            old_name='rate',
            new_name='bonus',
        ),
    ]
