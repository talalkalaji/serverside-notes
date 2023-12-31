# Generated by Django 4.2.6 on 2023-12-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('details', models.CharField(max_length=254, unique=True)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=12)),
                ('image', models.ImageField(upload_to='RawMaterials/')),
                ('price', models.DecimalField(decimal_places=3, max_digits=12)),
                ('quantity_price', models.DecimalField(decimal_places=3, max_digits=12)),
            ],
        ),
    ]
