# Generated by Django 3.0 on 2020-05-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0010_auto_20200529_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth',
            field=models.CharField(max_length=100),
        ),
    ]
