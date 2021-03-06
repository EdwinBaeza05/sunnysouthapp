# Generated by Django 3.1 on 2020-10-12 05:09

from django.db import migrations, models
import sunnysouth.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_generate_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='uuid',
            field=models.CharField(default=sunnysouth.utils.models.generate_uuid, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.CharField(default=sunnysouth.utils.models.generate_uuid, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='uuid',
            field=models.CharField(default=sunnysouth.utils.models.generate_uuid, max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='uuid',
            field=models.CharField(default=sunnysouth.utils.models.generate_uuid, max_length=300, unique=True),
        ),
    ]
