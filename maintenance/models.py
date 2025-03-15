from django.db import models
from django.utils import timezone
from operations.models import Shift, Area

class IssueType(models.Model):
    """Model to represent types of issues (electrical or mechanical)"""
    CATEGORY_CHOICES = [
        ('ELECTRICAL', 'Electrical'),
        ('MECHANICAL', 'Mechanical'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"

class MaintenanceIssue(models.Model):
    """Model to represent maintenance issues reported by engineers"""
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
    description = models.TextField()
    reported_by = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolution_notes = models.TextField(blank=True, null=True)
    resolution_timestamp = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.issue_type} - {self.shift}"
    
    def resolve(self, notes):
        """Mark the issue as resolved with notes and timestamp"""
        self.resolved = True
        self.resolution_notes = notes
        self.resolution_timestamp = timezone.now()
        self.save()

class PlannedMaintenance(models.Model):
    """Model to represent planned maintenance activities by general shift engineers"""
    STATUS_CHOICES = [
        ('COMPLETED', 'Completed'),
        ('IN_PROGRESS', 'Under Progress'),
        ('PENDING', 'Pending'),
    ]
    
    CATEGORY_CHOICES = [
        ('ELECTRICAL', 'Electrical'),
        ('MECHANICAL', 'Mechanical'),
    ]
    
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    planned_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)
    assigned_to = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
    
    def update_status(self, status, notes=None):
        """Update the status of the maintenance activity"""
        self.status = status
        if notes:
            self.notes = notes
        if status == 'COMPLETED':
            self.completion_date = timezone.now().date()
        self.save() 