# Generated by Django 4.1.3 on 2023-08-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_user',
            name='account_number',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
