from django.contrib import admin
from django.urls import path
from .views import PageListView, PageFormView


urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    path('newpage/', PageFormView.as_view(), name='page-form'),

]