from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)  # 设置默认值为当前日期
    category = models.CharField(max_length=100, default='General')  # 设置默认值

    def __str__(self):
        return self.description
