# Generated by Django 3.0.8 on 2020-07-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_projectlink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='longDescription',
        ),
        migrations.AddField(
            model_name='project',
            name='shortDescription',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
