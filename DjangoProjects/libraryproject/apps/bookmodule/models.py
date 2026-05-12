#### LAB 8
# from django.db import models

# # Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     price = models.FloatField(default = 0.0)
#     edition = models.SmallIntegerField(default = 1)

# class Address(models.Model):
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.city

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     address = models.ForeignKey(Address, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateField()
    rating = models.SmallIntegerField(default=1)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


# Keep these from Lab 8 if they still exist
class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name