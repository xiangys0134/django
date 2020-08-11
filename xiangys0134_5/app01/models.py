from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey('Publish',to_field="id",on_delete=models.CASCADE,null=True)
    author = models.ManyToManyField('Author',db_table='book2author')

class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    email = models.CharField(max_length=50)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    ad = models.OneToOneField('AuthorDetail',on_delete=models.CASCADE,null=True)

class AuthorDetail(models.Model):
    birthday = models.DateField()
    telephone = models.IntegerField()
    addr = models.CharField(max_length=64)

class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)