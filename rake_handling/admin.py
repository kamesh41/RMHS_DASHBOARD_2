from django.contrib import admin
from .models import RakeEntry, RakeNotification

@admin.register(RakeEntry)
class RakeEntryAdmin(admin.ModelAdmin):
    list_display = ('rake_id', 'material', 'wagon_tippler', 'quantity', 'status', 'arrival_time', 'completion_time', 'reported_by')
    list_filter = ('status', 'wagon_tippler', 'material')
    search_fields = ('rake_id', 'notes', 'reported_by')
    date_hierarchy = 'arrival_time'
    
    actions = ['mark_as_completed', 'mark_as_in_progress', 'mark_as_pending']
    
    def mark_as_completed(self, request, queryset):
        for rake in queryset:
            rake.update_status('COMPLETED')
    mark_as_completed.short_description = "Mark selected rakes as completed"
    
    def mark_as_in_progress(self, request, queryset):
        for rake in queryset:
            rake.update_status('IN_PROGRESS')
    mark_as_in_progress.short_description = "Mark selected rakes as in progress"
    
    def mark_as_pending(self, request, queryset):
        for rake in queryset:
            rake.update_status('PENDING')
    mark_as_pending.short_description = "Mark selected rakes as pending"

@admin.register(RakeNotification)
class RakeNotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'rake_entry', 'status', 'timestamp', 'is_read')
    list_filter = ('status', 'is_read', 'timestamp')
    search_fields = ('message',)
    date_hierarchy = 'timestamp'
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected notifications as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected notifications as unread" 