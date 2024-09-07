from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('add/', views.add, name='add'),
    path('singel/<int:id>/', views.singel_data, name='singel'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]