# Generated by Django 4.2.4 on 2023-08-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alter_registration_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='account_no',
            field=models.CharField(default=' ', max_length=16),
            preserve_default=False,
        ),
    ]
