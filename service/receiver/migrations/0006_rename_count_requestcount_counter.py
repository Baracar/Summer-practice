# Generated by Django 4.0.5 on 2022-06-29 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0005_requestcount_remove_request_metrics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestcount',
            old_name='count',
            new_name='counter',
        ),
    ]
