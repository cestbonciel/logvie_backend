# Generated by Django 2.2.5 on 2021-12-06 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logvie_app', '0005_auto_20211202_0133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diary',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-id']},
        ),
    ]
