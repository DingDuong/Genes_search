# Generated by Django 2.0.4 on 2018-04-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gene_app', '0008_auto_20180411_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='submitter_comment',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
