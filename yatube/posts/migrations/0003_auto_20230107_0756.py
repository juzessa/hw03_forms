# Generated by Django 2.2.19 on 2023-01-07 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models
                                    .deletion.CASCADE,
                                    related_name='posts', to='posts.Group'),
        ),
    ]
