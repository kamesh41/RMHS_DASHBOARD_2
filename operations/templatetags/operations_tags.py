from django import template
from operations.models import Area

register = template.Library()

@register.filter
def format_area_name(area):
    """
    Format area name to include sub-areas if it's a combined area
    """
    if area.is_combined and area.sub_areas:
        sub_areas = area.get_sub_areas()
        return f"{area.name} ({', '.join(sub_areas)})"
    return area.name

@register.simple_tag
def get_area_display_name(area_id):
    """
    Get the display name for an area by ID
    """
    try:
        area = Area.objects.get(id=area_id)
        return format_area_name(area)
    except Area.DoesNotExist:
        return "Unknown Area" 