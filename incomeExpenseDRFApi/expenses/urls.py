from django.urls import path
from .views import ExpenseDetail, ExpenseList

urlpatterns = [
    path('', ExpenseList.as_view(), name='expenses'),
    path('<int:id>', ExpenseDetail.as_view(), name='expense'),
]
