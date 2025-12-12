from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<int:room_id>/', views.room_details, name='room_details'),
    path('booking/', views.booking, name='booking'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/rooms/', views.admin_rooms, name='admin_rooms'),
    path('admin/bookings/', views.admin_bookings, name='admin_bookings'),
]
