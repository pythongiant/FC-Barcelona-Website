# Generated by Django 2.0.3 on 2018-03-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProgrammerProfile', '0008_auto_20180306_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Name',
            field=models.TextField(),
        ),
    ]
