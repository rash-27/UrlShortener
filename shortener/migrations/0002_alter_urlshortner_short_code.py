# Generated by Django 4.2.6 on 2023-10-25 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='short_code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]