# Generated by Django 3.1.1 on 2022-02-14 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20220111_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=100, primary_key=True, serialize=False)),
                ('ENA_GTIN', models.CharField(max_length=100)),
                ('description', models.CharField(default='unknown', max_length=100)),
                ('sku', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('reserved_stock', models.IntegerField()),
                ('available_stock', models.IntegerField()),
                ('min_stock', models.IntegerField()),
                ('max_stock', models.IntegerField()),
                ('low_stock', models.IntegerField()),
                ('stock_level', models.IntegerField()),
                ('reward', models.BooleanField(default=False)),
                ('point_needed', models.IntegerField()),
                ('taxation', models.CharField(max_length=100)),
                ('new_weight', models.CharField(max_length=100)),
                ('gross_weight', models.CharField(max_length=100)),
                ('added_in', models.CharField(max_length=100)),
                ('modified_in', models.DateTimeField(max_length=100)),
                ('commission', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('on_sale', models.BooleanField(default=False)),
                ('on_sale_init_day', models.DateTimeField()),
                ('on_sale_final_day', models.DateTimeField()),
                ('promotional', models.BooleanField()),
                ('status', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('bundle', models.CharField(max_length=100)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
