# Generated by Django 3.1.1 on 2022-02-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220214_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added_in',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='commission',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='gross_weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_in',
            field=models.DateTimeField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='new_weight',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_sale_final_day',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_sale_init_day',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='taxation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
