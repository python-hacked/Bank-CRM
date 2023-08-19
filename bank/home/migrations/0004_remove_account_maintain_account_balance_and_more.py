# Generated by Django 4.1.3 on 2023-08-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_account_maintain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_maintain',
            name='account_balance',
        ),
        migrations.AddField(
            model_name='register_user',
            name='account_balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
