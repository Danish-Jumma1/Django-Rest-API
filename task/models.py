from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    discription = models.CharField(max_length = 100)
    price = models.IntegerField(),
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title