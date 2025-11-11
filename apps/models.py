from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MessProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    is_day_scholar = models.BooleanField(default = True)
    amt_paid = models.FloatField(default = 0.0)
    def __str__(self):
        return f"MessProfile of {self.user.username}"

class MessVisit(models.Model):
    user = models.ForeignKey(MessProfile, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=32)   # e.g. "2025-11-10-LUNCH"
    entry_scanned_at = models.DateTimeField(null=True, blank=True)
    exit_scanned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'session_id')

class OneTimeToken(models.Model):
    user = models.ForeignKey(MessProfile, on_delete=models.CASCADE)
    visit = models.ForeignKey(MessVisit, on_delete=models.CASCADE)
    token_type = models.CharField(max_length=10)  # entry / exit / temp
    token = models.CharField(max_length=512, unique=True)
    device_id = models.CharField(max_length=128)   # prevent sharing
    gate_id = models.CharField(max_length=32)
    used = models.BooleanField(default=False)
    expires_at = models.DateTimeField()
