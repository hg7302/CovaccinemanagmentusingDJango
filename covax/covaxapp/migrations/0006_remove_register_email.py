# Generated by Django 3.2 on 2021-04-18 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covaxapp', '0005_alter_stock_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='email',
        ),
    ]
