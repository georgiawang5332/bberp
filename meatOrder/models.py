from django.db import models
import django.utils.timezone as timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MeatProductName(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='項號')
    meatID = models.IntegerField(verbose_name='肉品編號')
    meatName = models.CharField(max_length=30, verbose_name='名稱')

    def __str__(self):
        return self.meatName

    class Meta:
        # ordering = ['-name']
        verbose_name_plural = _('肉品商品名稱')


class SupplierName(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='項號')
    supplier_name = models.CharField(max_length=100, blank=True, verbose_name='供應商名稱')

    def __str__(self):
        return self.supplier_name

    class Meta:
        # ordering = ['-name']
        verbose_name_plural = _('供應商名稱')


class MeatOrder(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='項號')
    order_number = models.CharField(max_length=200, blank=True, verbose_name='訂單編號')
    product_name = models.ForeignKey(MeatProductName, on_delete=models.CASCADE, verbose_name='商品名稱')
    quantity = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name='數量')
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name='單價')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='小計')
    remark = models.TextField(max_length=500, blank=False, null=False, verbose_name='備註')
    supplier_name = models.ForeignKey(SupplierName, on_delete=models.CASCADE, verbose_name='供應廠商名稱')
    procurement_staff = models.CharField(max_length=20, blank=True, verbose_name='採購人員')

    add_date = models.DateTimeField('儲存日期', default=timezone.now, blank=True)
    mod_date = models.DateTimeField('最後修改日期', auto_now=True, blank=True)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        # ordering = ['-name']
        verbose_name_plural = _('肉品訂購')
        db_table = "emp"
#
# 多元化商品可能我就需要ManyToManyField來救我了 XDDDDDDDDDDDD
# class Journal(models.Model):
#     title = models.CharField(max_length=120)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category)
#     publish_date = models.DateTimeField()
#     views = models.IntegerField(default=0)
#     reviewed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
