# Generated by Django 3.1.1 on 2022-02-17 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20220217_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.CharField(auto_created=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
