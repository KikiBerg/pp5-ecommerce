from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    # Additional fields specific to seeds
    botanical_name = models.CharField(max_length=254, null=True, blank=True)
    is_organic = models.BooleanField(default=False)
    days_to_maturity = models.IntegerField(null=True, blank=True)
    lifespan = models.CharField(max_length=50, null=True, blank=True)
    sowing_season = models.CharField(max_length=100, null=True, blank=True)
    sowing_depth = models.CharField(max_length=50, null=True, blank=True)
    germination_time = models.CharField(max_length=100, null=True, blank=True)
    sunlight_requirement = models.CharField(max_length=100, null=True, blank=True)
    water_requirement = models.CharField(max_length=100, null=True, blank=True)
    plant_spacing = models.CharField(max_length=50, null=True, blank=True)
    row_spacing = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    harvest_blooming = models.CharField(max_length=100, null=True, blank=True)
    seed_count = models.IntegerField(null=True, blank=True)    
    instructions = models.TextField(null=True, blank=True)
    # Additional fields for gardening supplies
    is_gardening_supply = models.BooleanField(default=False)    
    dimensions = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
