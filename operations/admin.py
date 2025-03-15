from django.contrib import admin
from .models import Area, Shift, Material, FeedingOperation, ReclaimingOperation, CrushingOperation, ReceivingOperation, DailySummary

class OperationBaseAdmin(admin.ModelAdmin):
    list_filter = ('area', 'shift', 'material')
    search_fields = ('notes',)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_combined')
    search_fields = ('name',)

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(FeedingOperation)
class FeedingAdmin(OperationBaseAdmin):
    list_display = ('material', 'area', 'shift', 'quantity', 'destination', 'timestamp')

@admin.register(ReclaimingOperation)
class ReclaimingAdmin(OperationBaseAdmin):
    list_display = ('material', 'area', 'shift', 'quantity', 'source', 'timestamp')

@admin.register(CrushingOperation)
class CrushingAdmin(OperationBaseAdmin):
    list_display = ('material', 'area', 'shift', 'quantity', 'crusher', 'timestamp')

@admin.register(ReceivingOperation)
class ReceivingAdmin(OperationBaseAdmin):
    list_display = ('material', 'area', 'shift', 'quantity', 'source', 'timestamp')

@admin.register(DailySummary)
class DailySummaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'area', 'total_feeding', 'total_reclaiming', 'total_crushing', 'total_receiving')
    list_filter = ('date', 'area')
    date_hierarchy = 'date'
