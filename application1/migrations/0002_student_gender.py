# Generated by Django 3.2.12 on 2022-02-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
