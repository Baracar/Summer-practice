# Generated by Django 4.0.5 on 2022-06-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metrics',
            name='host',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
