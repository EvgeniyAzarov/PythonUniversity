from django.urls import path
from . import views

app_name = 'bills'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:bill_id>/', views.bill, name='bill'),
    path('delete/<int:bill_id>/', views.delete, name='delete')
]
