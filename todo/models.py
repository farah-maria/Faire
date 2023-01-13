from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    header = models.CharField(max_length=210, null=True)
    info = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.header

    class Meta:
        ordering = ['done']