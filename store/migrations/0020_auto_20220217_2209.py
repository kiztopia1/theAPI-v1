# Generated by Django 3.1.1 on 2022-02-17 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20220217_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='items',
            new_name='products',
        ),
    ]
