from django.contrib import admin
from django.urls import path, include
from .views import ArticleViewSet, AuthorProfileViewSet
from.import views
from rest_framework.routers import DefaultRouter, SimpleRouter 

router = DefaultRouter()
router.register('Article', ArticleViewSet, basename='router_register_drfapp')

router.register('AuthorProfile', AuthorProfileViewSet, basename='AuthorProfile')


urlpatterns = [
       path('api/', include((router.urls, 'drfapp'), namespace='api_folder_urls')),
]