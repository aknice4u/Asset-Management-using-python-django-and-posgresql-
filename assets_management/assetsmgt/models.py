from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    date_added = models.DateField(default=timezone.now)


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)


class Assets(models.Model):
    assetname = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    year_purchased = models.CharField(max_length=200)
    amount_purchased = models.FloatField(default=0.00)
    current_value_amount = models.DecimalField(default=0.00, max_digits=11, decimal_places=2)
    condition = models.CharField(max_length=200)
    quantity = models.BigIntegerField(default=0)
    is_disposed = models.IntegerField(default=0)
    date_disposed = models.DateField(default=timezone.now)
    warranty_end_date = models.DateField(default=timezone.now)
    photo_path = models.CharField(max_length=200, default='')


class AssetsLocation(models.Model):
    holder_name = models.CharField(max_length=100)
    assets_location = models.CharField(max_length=100)
    date_issued = models.DateField()
    purpose = models.TextField()
    update_at = models.DateField()


class CompanyBranch(models.Model):
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    user_id = models.CharField(max_length=255)
    update_at = models.DateField()


class Department(models.Model):
    department = models.CharField(max_length=100)
    description = models.TextField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    branchId = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    updated_at = models.DateField()


class ItemAssignment(models.Model):
    asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    condition = models.CharField(max_length=50)
    remark = models.TextField()
    date_assigned = models.DateField()


class AssetTransfer(models.Model):
    transferred_from = models.IntegerField()
    transferred_to = models.IntegerField()
    asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    remark = models.TextField()
    date_transferred = models.DateField()
    initiated_by = models.IntegerField


class AssetPurchase(models.Model):
    Name = models.CharField(max_length=200)
    categoryId = models.asset_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(CompanyBranch, on_delete=models.CASCADE)
    date_Supplied = models.DateField()
    cost = models.FloatField()
    condition = models.CharField(max_length=200)
    quantity = models.IntegerField()
    supplier = models.IntegerField()
    status = models.IntegerField()


class MaintenanceHistory(models.Model):
    assetId = models.asset_id = models.ForeignKey(Assets, on_delete=models.CASCADE)
    issue = models.TextField()
    fixing_price = models.FloatField()
    fixed_by = models.IntegerField()
    date_fixed = models.DateField()
