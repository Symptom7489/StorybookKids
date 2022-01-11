from django.contrib import admin
from django.urls import path
from .views import PageListView


urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
]