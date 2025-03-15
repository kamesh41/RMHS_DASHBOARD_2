from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='operations_dashboard'),
    path('feeding/', views.feeding_view, name='feeding'),
    path('reclaiming/', views.reclaiming_view, name='reclaiming'),
    path('crushing/', views.crushing_view, name='crushing'),
    path('receiving/', views.receiving_view, name='receiving'),
    path('daily_summary/', views.daily_summary_view, name='daily_summary'),
    path('export_data/', views.export_data, name='export_operations_data'),
] 