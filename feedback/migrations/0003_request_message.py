# Generated by Django 3.1.2 on 2020-11-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
    ]
