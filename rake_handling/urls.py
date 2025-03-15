from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.rake_dashboard, name='rake_dashboard'),
    path('rake_entry/', views.rake_entry_view, name='rake_entry'),
    path('notifications/', views.notifications_view, name='rake_notifications'),
    path('update_rake_status/<int:rake_id>/', views.update_rake_status, name='update_rake_status'),
    path('mark_notification_read/<int:notification_id>/', views.mark_notification_read, name='mark_notification_read'),
    path('export_data/', views.export_rake_data, name='export_rake_data'),
] 