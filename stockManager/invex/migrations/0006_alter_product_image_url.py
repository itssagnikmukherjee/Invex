# Generated by Django 5.1.6 on 2025-02-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invex', '0005_alter_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
