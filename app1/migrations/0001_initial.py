# Generated by Django 3.0.6 on 2020-06-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=25)),
                ('Last_Name', models.CharField(max_length=25)),
                ('Email_Id', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=150)),
            ],
        ),
    ]
