from django.urls import path
from .views import AttendanceListCreateView, AttendanceRetrieveUpdateDestroyView





urlpatterns = [
    path('attendances/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendances/<int:pk>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='attendance-detail'),
  
]   
