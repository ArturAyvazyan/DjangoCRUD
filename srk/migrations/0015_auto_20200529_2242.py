# Generated by Django 3.0 on 2020-05-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srk', '0014_auto_20200529_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='bows/'),
        ),
    ]
