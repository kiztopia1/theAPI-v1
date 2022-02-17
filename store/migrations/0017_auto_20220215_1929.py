# Generated by Django 3.1.1 on 2022-02-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20220215_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='store.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_supplier',
            field=models.ManyToManyField(null=True, to='store.Supplier'),
        ),
    ]
