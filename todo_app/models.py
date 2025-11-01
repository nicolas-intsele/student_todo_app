from django.db import models
from django.utils import timezone
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    due_time = models.TimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk':self.pk})
