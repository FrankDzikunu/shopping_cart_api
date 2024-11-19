from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_thumbnail = models.URLField(verbose_name="Thumbnail Image URL")
    image_mobile = models.URLField(verbose_name="Mobile Image URL")
    image_tablet = models.URLField(verbose_name="Tablet Image URL")
    image_desktop = models.URLField(verbose_name="Desktop Image URL")
    stock = models.PositiveIntegerField(default=0) 
    description = models.TextField(blank=True, null=True)  

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['name']

    def __str__(self):
        return self.name

    def is_in_stock(self):
                return self.stock > 0
