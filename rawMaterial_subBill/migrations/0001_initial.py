# Generated by Django 4.2.6 on 2023-12-19 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rawmaterials', '0002_alter_rawmaterial_price_alter_rawmaterial_quantity_and_more'),
        ('sup_bill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterialSupplierBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('edit_date', models.DateField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('rawPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantityPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('rawMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rawmaterials.rawmaterial')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sup_bill.billsupplier')),
            ],
            options={
                'db_table': 'RawMaterialSupplierBill',
            },
        ),
    ]
