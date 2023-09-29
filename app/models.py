from django.db import models

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Details(models.Model):
#     name = models.CharField(max_length=100)
#     notes = models.TextField()
#     category = models.ForeignKey(Category, related_name="detail", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    


class Product(models.Model):
    category = models.ManyToManyField(Category, db_index=True, related_name="product")
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)



    def __str__(self):
        return self.name


