from django.contrib import admin
from .models import IssueType, MaintenanceIssue, PlannedMaintenance

@admin.register(IssueType)
class IssueTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')

@admin.register(MaintenanceIssue)
class MaintenanceIssueAdmin(admin.ModelAdmin):
    list_display = ('issue_type', 'area', 'shift', 'reported_by', 'timestamp', 'resolved')
    list_filter = ('issue_type__category', 'area', 'shift', 'resolved')
    search_fields = ('description', 'reported_by', 'resolution_notes')
    date_hierarchy = 'timestamp'
    
    actions = ['mark_as_resolved']
    
    def mark_as_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_as_resolved.short_description = "Mark selected issues as resolved"

@admin.register(PlannedMaintenance)
class PlannedMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'area', 'category', 'status', 'planned_date', 'completion_date', 'assigned_to')
    list_filter = ('status', 'category', 'area', 'planned_date')
    search_fields = ('title', 'description', 'assigned_to', 'notes')
    date_hierarchy = 'planned_date'
    
    actions = ['mark_as_completed', 'mark_as_in_progress', 'mark_as_pending']
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='COMPLETED')
    mark_as_completed.short_description = "Mark selected activities as completed"
    
    def mark_as_in_progress(self, request, queryset):
        queryset.update(status='IN_PROGRESS')
    mark_as_in_progress.short_description = "Mark selected activities as in progress"
    
    def mark_as_pending(self, request, queryset):
        queryset.update(status='PENDING')
    mark_as_pending.short_description = "Mark selected activities as pending" 