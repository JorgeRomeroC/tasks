from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']