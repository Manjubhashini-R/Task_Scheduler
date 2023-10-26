from django.db import models

class Newapp(models.Model):
    PRIORITY_CHOICES = [
        ('top', 'Top Priority'),
        ('middle', 'Middle Priority'),
        ('low', 'Less Priority'),
    ]

    task = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='top')
    deadline = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task


