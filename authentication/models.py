from django.contrib.auth.models import AbstractUser
from django.db import models
from forums.models import Post
# Create your models here.

class MyUser(AbstractUser):
    B2024 = 2023
    Y2024 = 2024
    Y2025 = 2025
    Y2026 = 2026
    A2026 = 2027
    TERM1 = 1
    TERM2 = 2
    TERM3 = 3
    YEAR_CHOICES = [
        (B2024, 'before 2024'),
        (Y2024, '2024'),
        (Y2025, '2025'),
        (Y2026, '2026'),
        (A2026, 'after 2026'),
    ]
    TERM_CHOICES = [
        (TERM1, '1'),
        (TERM2, '2'),
        (TERM3, '3'),
    ]
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    admission_year = models.IntegerField(choices=YEAR_CHOICES, null=True)
    admission_term = models.IntegerField(choices=TERM_CHOICES, null=True)
    future_major = models.CharField(max_length=100, null=True)