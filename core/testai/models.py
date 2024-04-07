from django.db import models

class Tests(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    steps = models.TextField()

    class Meta:
        ordering = ['created']
