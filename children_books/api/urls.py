from django.urls import path,include
from rest_framework import routers
from children_books.api import views
from children_books.api.views import registration_view

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'page', views.PageViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registration', registration_view, name='register')
]