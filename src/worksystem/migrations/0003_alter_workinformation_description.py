# Generated by Django 4.1 on 2022-08-18 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worksystem', '0002_alter_workinformation_time_estimation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workinformation',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
