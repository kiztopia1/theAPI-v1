# Generated by Django 3.1.1 on 2022-03-02 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20220302_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='seller',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]