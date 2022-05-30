from django.urls import path
from .views import IncomeDetail, IncomeList

urlpatterns = [
    path('', IncomeList.as_view(), name='incomes'),
    path('<int:id>', IncomeDetail.as_view(), name='income'),
]
