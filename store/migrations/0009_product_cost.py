# Generated by Django 3.1.1 on 2022-02-15 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220215_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.CharField(default='0', max_length=100),
        ),
    ]