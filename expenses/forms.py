from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'date']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone_number', 'birthday')  # 添加额外的字段

    # 如果需要，可以在这里添加字段的自定义验证
