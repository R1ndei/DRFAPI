from django.urls import path
from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats

urlpatterns = [
    path('expense_category_data', ExpenseSummaryStats.as_view(), name='expense_category_data'),
    path('income_category_data', IncomeSourcesSummaryStats.as_view(), name='income_category_data'),
]
