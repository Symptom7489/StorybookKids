from django.urls import path,include
from rest_framework import routers
from storybook_api import views

router = routers.DefaultRouter()
router.register(r'book',views.BookViewSet)
router.register(r'author',views.AuthorViewSet)
router.register(r'page',views.PageViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]