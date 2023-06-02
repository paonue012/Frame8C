# Generated by Django 3.2.12 on 2022-02-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('second_name', models.CharField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
