# Generated by Django 4.2.6 on 2023-12-06 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rawmaterials', '0002_alter_rawmaterial_price_alter_rawmaterial_quantity_and_more'),
        ('products', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rawmaterial_quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rawmaterials.rawmaterial')),
            ],
            options={
                'db_table': 'RawMaterial_Product',
            },
        ),
    ]
