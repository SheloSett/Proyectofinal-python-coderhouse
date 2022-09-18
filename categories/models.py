from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to = "categories/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Category(models.Model):
    name = models.CharField(max_length=50)