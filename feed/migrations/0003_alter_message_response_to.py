# Generated by Django 5.0.6 on 2024-06-13 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_message_response_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='response_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.message'),
        ),
    ]