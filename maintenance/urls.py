from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.maintenance_dashboard, name='maintenance_dashboard'),
    path('electrical_issues/', views.electrical_issues_view, name='electrical_issues'),
    path('mechanical_issues/', views.mechanical_issues_view, name='mechanical_issues'),
    path('planned_maintenance/', views.planned_maintenance_view, name='planned_maintenance'),
    path('update_issue_status/<int:issue_id>/', views.update_issue_status, name='update_issue_status'),
    path('update_planned_status/<int:planned_id>/', views.update_planned_status, name='update_planned_status'),
    path('export_data/', views.export_maintenance_data, name='export_maintenance_data'),
] 