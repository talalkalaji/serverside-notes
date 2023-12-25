# Generated by Django 4.2.6 on 2023-12-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawmaterials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='quantity_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterModelTable(
            name='rawmaterial',
            table='RawMaterial',
        ),
    ]
