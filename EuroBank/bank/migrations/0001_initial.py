# Generated by Django 4.2.4 on 2023-08-17 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('idnumber', models.IntegerField()),
                ('id_img', models.ImageField(upload_to='idimage')),
            ],
        ),
    ]
