from django.db import models

# Create your models here.
# class Author(models.Model):
#     name=models.CharField(max_length=100)

#     def __str__(self):
#         return self.name



# class Book(models.Model):
#     name=models.CharField(max_length=100)
#     author=models.ForeignKey(Author,on_delete=models.CASCADE)
#     price=models.DecimalField(max_digits=6,decimal_places=2)
#     published_date=models.DateField()

#     def __str__(self):
#         return self.name

class Task(models.Model):
    body=models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:20]