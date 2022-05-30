from django.db import models
from authentication.models import User


class Expense(models.Model):
    CATEGORY_OPTIONS = [
        ('GAMES', 'GAMES'),
        ('FOOD', 'FOOD'),
        ('TRAVEL', 'TRAVEL'),
        ('HOUSE', 'HOUSE'),
        ('OTHER', 'OTHER'),
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return f"{self.owner}s expense"