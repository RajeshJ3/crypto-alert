from django.db import models

class Alert(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='alert_user')
    currency = models.ForeignKey('currencies.Currency', on_delete=models.CASCADE, related_name='alert_currency')

    ABOVE_OR_BELOW_CHOICES = (
        ('Above', 'Above'),
        ('Below', 'Below'),
    )
    above_or_below = models.CharField(max_length=10, choices=ABOVE_OR_BELOW_CHOICES)
    price = models.FloatField()
    price_in = models.ForeignKey('currencies.Currency', on_delete=models.CASCADE, related_name='alert_price_in')
    on_platform = models.ForeignKey('utils.Platform', on_delete=models.CASCADE, related_name='alert_on_platform')

    is_completed = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.user)
