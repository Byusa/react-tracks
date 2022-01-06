from typing import Optional
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Track(models.Model):
    # id field is added automatically
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)  # it can be empty
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
