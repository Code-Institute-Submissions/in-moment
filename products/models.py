from django.db import models

# Create your models here.
# Category model.
class Category(models.Model):
    # Changing plural name of category on admin panel.
    class Meta:
        verbose_name_plural = "Categories"
    # Model fields.
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    # Overriding to string method.
    def __str__(self):
        return self.name
    # Method returning friendly name of a category.
    def get_friendly_name(self):
        return self.friendly_name
# Product model.
class Product(models.Model):
    # Product fields.
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    # Overriding to string method.
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey("Product", null=False, blank=False, on_delete=models.CASCADE)
    body = models.CharField(max_length=254, null=False, blank=False)
