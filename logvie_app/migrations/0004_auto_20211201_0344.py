# Generated by Django 2.2.5 on 2021-12-01 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logvie_app', '0003_auto_20211201_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='writing_date',
            field=models.CharField(max_length=128),
        ),
    ]