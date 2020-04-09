# Generated by Django 3.0.5 on 2020-04-09 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published_date',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='updated_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='published_date'),
        ),
    ]
