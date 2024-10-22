# Generated by Django 5.1.1 on 2024-10-10 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentwork',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='save_work.group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='save_work.group'),
        ),
    ]
