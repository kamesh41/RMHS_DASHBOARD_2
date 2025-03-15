from django.db import models
from django.utils import timezone

class Area(models.Model):
    """Model to represent areas in the plant"""
    name = models.CharField(max_length=100)
    is_combined = models.BooleanField(default=False)
    sub_areas = models.TextField(blank=True, null=True)  # Store sub-area names as comma-separated values
    
    def __str__(self):
        return self.name
    
    def get_sub_areas(self):
        if self.sub_areas:
            return self.sub_areas.split(',')
        return []

class Shift(models.Model):
    """Model to represent shifts in the plant"""
    SHIFT_CHOICES = [
        ('A', 'Shift A'),
        ('B', 'Shift B'),
        ('C', 'Shift C'),
    ]
    
    name = models.CharField(max_length=1, choices=SHIFT_CHOICES)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.get_name_display()} - {self.date}"
    
    class Meta:
        unique_together = ['name', 'date']

class MaterialType(models.Model):
    """Model to represent types of materials (categories)"""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Material(models.Model):
    """Material model for tracking different materials"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(MaterialType, on_delete=models.SET_NULL, null=True, blank=True, related_name='materials')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert name to uppercase for consistency
        self.name = self.name.upper()
        super().save(*args, **kwargs)

# Base class for all operations
class OperationBase(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    reported_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        abstract = True

class FeedingOperation(OperationBase):
    """Model to represent feeding operations"""
    destination = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Feeding: {self.material} - {self.quantity} tons - {self.shift}"

class ReclaimingOperation(OperationBase):
    """Model to represent reclaiming operations"""
    source = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Reclaiming: {self.material} - {self.quantity} tons - {self.shift}"

class CrushingOperation(OperationBase):
    """Model to represent crushing operations"""
    crusher = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Crushing: {self.material} - {self.quantity} tons - {self.shift}"

class ReceivingOperation(OperationBase):
    """Model to represent receiving operations"""
    source = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Receiving: {self.material} - {self.quantity} tons - {self.shift}"

class DailySummary(models.Model):
    """Model to store daily summaries of operations"""
    date = models.DateField(unique=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    total_feeding = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_reclaiming = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_crushing = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_receiving = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Summary for {self.date} - {self.area}"
