from django.urls import path
from bills import views

app_name = 'bills'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:bill_id>/', views.bill_view, name='bill'),
    path('delete/<int:bill_id>/', views.delete, name='delete'),
    path('data/download-json/', views.export_data, {'action': 'downloadJson'}),
    path('data/preview-json/', views.export_data, {'action': 'previewJson'}),
    path('data/download-xml/', views.export_data, {'action': 'downloadXml'}),
    path('data/preview-xml/', views.export_data, {'action': 'previewXml'})
]
