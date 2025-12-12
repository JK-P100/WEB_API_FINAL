from django.contrib import admin
from django.urls import path, include
from views import views

urlpatterns = [
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
    path("admin-panel/", admin.site.urls),
    path("", include("views.urls")),
]
