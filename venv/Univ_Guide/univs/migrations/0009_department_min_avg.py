# Generated by Django 4.2.10 on 2024-02-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univs', '0008_department_dtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='min_avg',
            field=models.IntegerField(null=True),
        ),
    ]
