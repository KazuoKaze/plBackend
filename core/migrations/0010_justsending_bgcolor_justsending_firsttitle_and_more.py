# Generated by Django 5.0.3 on 2024-03-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_modelproductmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='justsending',
            name='bgColor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='firstTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='orThirdModeTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='orsThirdModeTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='pThordTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='pTitleFirst',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='pTitleSecond',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='productModelImage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='justsending',
            name='productModelSecondImage',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='justsending',
            name='secondModerTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='secondsModerTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='textColor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='thirdModelTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='justsending',
            name='thirdsModelTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]