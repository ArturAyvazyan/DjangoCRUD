# Generated by Django 3.0 on 2020-05-29 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0006_auto_20200528_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age1',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.BooleanField(default=False),
        ),
    ]
