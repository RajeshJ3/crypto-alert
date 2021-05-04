from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=120, unique=True)
    logo = models.URLField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
