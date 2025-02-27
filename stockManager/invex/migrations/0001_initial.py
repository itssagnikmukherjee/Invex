# Generated by Django 5.1.6 on 2025-02-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('supplier', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
