# Generated by Django 3.2.7 on 2021-11-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('self', models.CharField(max_length=200)),
            ],
        ),
    ]
