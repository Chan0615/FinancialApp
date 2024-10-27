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


class CustomUser(AbstractUser):
    # 添加电话号码字段，使用US电话格式
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # 添加生日字段
    birthday = models.DateField(null=True, blank=True)

    # 可以添加更多的字段，例如：
    # website = models.URLField(max_length=200, blank=True)
    # bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        # 这将返回用户名，你也可以选择返回其他信息，比如 email 等
        return self.username
