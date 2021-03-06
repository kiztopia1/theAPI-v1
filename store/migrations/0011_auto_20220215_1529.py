# Generated by Django 3.1.1 on 2022-02-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(to='store.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='store.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_supplier',
            field=models.ManyToManyField(to='store.Supplier'),
        ),
    ]
