# Generated by Django 3.0 on 2020-06-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0020_auto_20200530_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, choices=[('Tech', 'Tech'), ('Buh', 'Buh'), ('Jah', 'Jah')], max_length=100, null=True),
        ),
    ]
