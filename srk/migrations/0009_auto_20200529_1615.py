# Generated by Django 3.0 on 2020-05-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0008_auto_20200529_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='ageo',
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='udalec',
            field=models.BooleanField(default=False),
        ),
    ]
