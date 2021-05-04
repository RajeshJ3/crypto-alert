from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=120, unique=True)
    logo = models.URLField(max_length=255, blank=True, null=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.code
