# Generated by Django 4.0.5 on 2022-06-28 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0003_alter_metrics_counter_alter_metrics_maxtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
