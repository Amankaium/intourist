# Generated by Django 3.2 on 2021-04-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
