from django.db import models

class Tests(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    description = models.TextField()

    class Meta:
        ordering = ['created']

class TestCase(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    test = models.ForeignKey(
        Tests,
        on_delete=models.CASCADE,
        related_name='tests'
    )

    class Meta:
        ordering = ['created']

class TestStep(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, default='')
    description = models.TextField()
    testcase = models.ForeignKey(
        TestCase,
        on_delete=models.CASCADE,
        related_name='steps'
    )

    class Meta:
        ordering = ['created']