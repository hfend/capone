# Generated by Django 3.1.5 on 2021-02-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capone', '0002_django_2_and_3_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='name',
            field=models.CharField(help_text='Name of this ledger', max_length=255),
        ),
    ]
