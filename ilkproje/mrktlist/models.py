from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=40,verbose_name="Alınacak")
    completed=models.BooleanField(verbose_name="Durum")

    def __str__(self):
        return self.title

