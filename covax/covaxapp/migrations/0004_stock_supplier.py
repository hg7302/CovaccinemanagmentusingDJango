# Generated by Django 3.2 on 2021-04-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covaxapp', '0003_auto_20210416_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('Vaccine_name', models.CharField(max_length=30)),
                ('Locality', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Quantity_departed', models.IntegerField()),
                ('Quantity_Remaning', models.IntegerField()),
                ('Supplier_regNo', models.IntegerField()),
            ],
            options={
                'db_table': 'STOCK',
            },
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('Supplier_regNO', models.IntegerField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=30)),
                ('SAddress', models.CharField(max_length=30)),
                ('Telephone_number', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'SUPPLIERS',
            },
        ),
    ]
