# Generated by Django 4.2.6 on 2023-12-24 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('table', '0003_remove_table_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField()),
                ('leaving_time', models.DateTimeField()),
                ('sits', models.IntegerField()),
                ('time_cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.table')),
            ],
            options={
                'db_table': 'Bill',
                'ordering': ['table', 'entry_time'],
            },
        ),
    ]
