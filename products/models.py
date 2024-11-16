from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_thumbnail = models.URLField()
    image_mobile = models.URLField()
    image_tablet = models.URLField()
    image_desktop = models.URLField()

    def __str__(self):
        return self.name
