# Generated by Django 4.1.1 on 2022-09-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iid', models.CharField(max_length=5)),
                ('iname', models.CharField(max_length=30)),
            ],
        ),
    ]
