from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    publish = models.CharField(max_length=30)
    author = models.CharField(max_length=30,null=True)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'









