from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True, unique=True)
    post_name = models.CharField(max_length=100)
    post_content = models.TextField()

    def __str__(self):
       return f'post_name: {self.post_name}'

