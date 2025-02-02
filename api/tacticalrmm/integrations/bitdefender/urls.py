from django.urls import path, include
from . import views


urlpatterns = [ 
    path('endpoints/', views.GetEndpoints.as_view()), 
    path('endpoint/<str:endpoint_id>/', views.GetEndpoint.as_view()),
    path('packages/', views.GetPackages.as_view()),
    path('endpoint/quickscan/<str:endpoint_id>/', views.GetQuickScan.as_view()),
    path('endpoint/fullscan/<str:endpoint_id>/', views.GetFullScan.as_view()),
    path('endpoint/quarantine/<str:endpoint_id>/', views.GetEndpointQuarantine.as_view()),
    path('quarantine/', views.GetQuarantine.as_view()),
    path('tasks/', views.GetTasks.as_view()),
    path('reports/', views.GetReportsList.as_view()),
    path('reports/create/<str:endpoint_id>/', views.GetCreateReport.as_view()),
    path('reports/delete/<str:report_id>/', views.GetDeleteReport.as_view())
]