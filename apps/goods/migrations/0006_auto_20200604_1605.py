# Generated by Django 2.2 on 2020-06-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20200604_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylookupvalue',
            name='display_sequence',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='data increment'),
        ),
    ]
