# Generated by Django 3.1 on 2022-04-22 00:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeatProductName',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='項號')),
                ('meatID', models.IntegerField(verbose_name='肉品編號')),
                ('meatName', models.CharField(max_length=30, verbose_name='名稱')),
            ],
            options={
                'verbose_name_plural': '肉品商品名稱',
            },
        ),
        migrations.CreateModel(
            name='SupplierName',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='項號')),
                ('supplier_name', models.CharField(blank=True, max_length=100, verbose_name='供應商名稱')),
            ],
            options={
                'verbose_name_plural': '供應商名稱',
            },
        ),
        migrations.CreateModel(
            name='MeatOrder',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='項號')),
                ('order_number', models.CharField(blank=True, max_length=200, verbose_name='訂單編號')),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='數量')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='單價')),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='小計')),
                ('remark', models.TextField(max_length=500, verbose_name='備註')),
                ('procurement_staff', models.CharField(blank=True, max_length=20, verbose_name='採購人員')),
                ('add_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='儲存日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最後修改日期')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meatOrder.meatproductname', verbose_name='商品名稱')),
                ('supplier_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meatOrder.suppliername', verbose_name='供應廠商名稱')),
            ],
            options={
                'verbose_name_plural': '肉品訂購',
                'db_table': 'emp',
            },
        ),
    ]
