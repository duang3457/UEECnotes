from django.db import models

from authentication.models import MyUser


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True, unique=True)
    post_name = models.CharField(max_length=100)
    post_content = models.TextField()
    post_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    post_by_name = models.CharField(max_length=100, null=True)

    def __str__(self):
       return f'post_name: {self.post_name}'

