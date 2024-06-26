# Generated by Django 5.0.3 on 2024-04-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_orderitem_options_remove_orderitem_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'Order Details'},
        ),
        migrations.AlterModelOptions(
            name='orderitemproduct',
            options={'verbose_name_plural': 'Order'},
        ),
        migrations.AddField(
            model_name='justsending',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
