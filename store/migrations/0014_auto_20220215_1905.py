# Generated by Django 3.1.1 on 2022-02-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20220215_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=100),
        ),
    ]
