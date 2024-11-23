from django.urls import path
from . import views

urlpatterns = [
    path('', views.bmi_form, name='bmi_form'),
    path('statistics/', views.bmi_statistics, name='bmi_statistics'),
    path('generate/', views.generate_data, name='generate_data'),
    path('delete/', views.delete_data, name='delete_data'),
]