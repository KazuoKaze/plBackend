# Generated by Django 5.0.3 on 2024-03-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_variant_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='justsending',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
