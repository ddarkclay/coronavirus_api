from django.db import models
from django.utils import timezone


class SupportModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=16)
    amount = models.FloatField()
    status = models.BooleanField(default=False)
    status_msg = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'support_model'

    def __str__(self):
        return self.name
