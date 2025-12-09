from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class FarmUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Livestock(models.Model):
    category = models.CharField(max_length=50)  # e.g., Cattle, Poultry
    tagId = models.CharField(max_length=100, unique=True)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField(help_text="Age in months")
    healthStatus = models.CharField(max_length=50, default='Healthy')
    location = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tagId} - {self.category}"

class Crop(models.Model):
    type = models.CharField(max_length=100)  # crop type e.g., Maize
    fieldLocation = models.CharField(max_length=150)
    plantingDate = models.DateField()
    expectedHarvestDate = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Growing')  # Growing, Ready, Harvested
    owner = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} ({self.fieldLocation})"

class Resource(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=100)  # Feed, Seed, Fertilizer, Equipment
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=50, default='kg')
    lastUpdated = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(FarmUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"

class VetRecord(models.Model):
    livestock = models.ForeignKey(Livestock, on_delete=models.SET_NULL, null=True, blank=True)
    livestockId = models.CharField(max_length=100, blank=True)  # store tagId if livestock not linked
    treatment = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    veterinarian = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    owner = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.treatment} - {self.date}"

class FinancialRecord(models.Model):
    TYPE_CHOICES = (('Income', 'Income'), ('Expense', 'Expense'))
    owner = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        sign = '+' if self.type == 'Income' else '-'
        return f"{self.date} {self.category} {sign}{self.amount}"

class MarketItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, default='Product')  # Product, Crop, Livestock
    description = models.TextField(blank=True)
    farmer = models.ForeignKey(FarmUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Ksh {self.price}"








# ROLE_CHOICES = (
# ('farmer','farmer'),
# ('customer','customer'),
# ('superuser','superuser'),
# )

# class User(AbstractUser):
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='farmer')
#
#     def __str__(self):
#         return f"{self.username} ({self.role})"

# class Livestock(models.Model):
#     category = models.CharField(max_length=50)  # e.g., Cattle, Poultry
#     tagId = models.CharField(max_length=100, unique=True)
#     breed = models.CharField(max_length=100)
#     age = models.PositiveIntegerField(help_text="Age in months")
#     healthStatus = models.CharField(max_length=50, default='Healthy')
#     location = models.CharField(max_length=150, blank=True, null=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livestock')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.tagId} - {self.category}"


