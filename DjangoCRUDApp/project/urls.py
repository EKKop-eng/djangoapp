
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("add/", views.add_item, name="add_item"),
    path("edit/<int:id>/", views.edit_item, name="edit_item"),
    path("delete/<int:id>/", views.delete_item, name="delete_item"),
]
