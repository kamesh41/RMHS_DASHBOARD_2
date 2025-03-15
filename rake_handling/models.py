from django.db import models
from django.utils import timezone
from operations.models import Material

# Completely redesigned model without area and shift fields
class RakeEntry(models.Model):
    """Model for rake entry data"""
    # Defining choices for status field
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    # Define choices for wagon tippler field
    WAGON_TIPPLER_CHOICES = [
        ('WT-1', 'Wagon Tippler 1'),
        ('WT-2', 'Wagon Tippler 2'),
        ('WT-3', 'Wagon Tippler 3'),
        ('WT-4', 'Wagon Tippler 4'),
    ]

    # Primary field - Wagon Tippler
    wagon_tippler = models.CharField(max_length=10, choices=WAGON_TIPPLER_CHOICES, default='WT-1')
    
    # Material handling
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='rake_entries')
    
    # Basic information
    rake_id = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    
    # Timestamps
    arrival_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)
    
    # Additional information
    notes = models.TextField(blank=True, null=True)
    reported_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Rake {self.rake_id} - {self.material.name} - {self.get_status_display()}"        

    def update_status(self, status, notes=None):
        """Update the status of a rake entry"""
        self.status = status

        # If status is COMPLETED, set completion time
        if status == self.COMPLETED and not self.completion_time:
            self.completion_time = timezone.now()

        # Add notes if provided
        if notes:
            if self.notes:
                self.notes += f"\n{timezone.now().strftime('%Y-%m-%d %H:%M')} - Status updated to {self.get_status_display()}: {notes}"
            else:
                self.notes = f"{timezone.now().strftime('%Y-%m-%d %H:%M')} - Status updated to {self.get_status_display()}: {notes}"

        self.save()

        # Create notification
        RakeNotification.objects.create(
            rake_entry=self,
            message=f"Rake {self.rake_id} at {self.get_wagon_tippler_display()} status updated to {self.get_status_display()}",
            status=status
        )

class RakeNotification(models.Model):
    """Model for rake notifications"""
    rake_entry = models.ForeignKey(RakeEntry, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    status = models.CharField(max_length=20, choices=RakeEntry.STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.message} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        ordering = ['-timestamp'] 