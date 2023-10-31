# Generated by Django 4.2.6 on 2023-10-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GB', '0008_rename_end_dist_fin_distrate_end_dist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TauxEmprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.FloatField(default=0)),
                ('end', models.FloatField(default=10)),
            ],
        ),
        migrations.RenameField(
            model_name='distrate',
            old_name='end_dist',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='distrate',
            old_name='start_dist',
            new_name='start',
        ),
        migrations.RenameField(
            model_name='yearrate',
            old_name='end_year',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='yearrate',
            old_name='start_year',
            new_name='start',
        ),
    ]