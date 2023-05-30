from django.db import models

class Feedback(models.Model):
    text = models.TextField()
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Feedback {self.id}"
