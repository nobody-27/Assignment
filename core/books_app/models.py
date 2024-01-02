from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100,help_text="Title")
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title