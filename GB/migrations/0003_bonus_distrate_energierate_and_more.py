# Generated by Django 4.2.6 on 2023-10-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GB', '0002_typerate_yearrate_remove_task_collections_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DistRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_dist', models.IntegerField()),
                ('end_dist_fin', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnergieRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energie', models.CharField(max_length=20)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='yearrate',
            old_name='year',
            new_name='end_year',
        ),
        migrations.AddField(
            model_name='yearrate',
            name='start_year',
            field=models.IntegerField(default=2023),
            preserve_default=False,
        ),
    ]
