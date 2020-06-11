from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from drfapp.models import *
from .serializers import ArticleSerializers, AuthorProfileSerializers
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination 
from django.db.models import Q
from django_filters import rest_framework as filters
from .permissions import ArticlePermission, AuthorProfilePermission



# from rest_framework.filters import(
# 	SearchFilter, 
# 	OrderingFilter
# 	)


class AuthorProfileViewSet(viewsets.ModelViewSet):
	queryset = AuthorProfile.objects.all()
	serializer_class = AuthorProfileSerializers
	permission_classes = [AuthorProfilePermission,]


class ArticleFilter(filters.FilterSet):
	#content = filters.CharField(lookup_expr='icontains')

	class Meta:
		model = Article
		fields = {
		'content':['icontains'],
		'created_by__username':['icontains'],
		}



class ArticleViewSet(viewsets.ModelViewSet):
	queryset  = Article.objects.all()
	serializer_class = ArticleSerializers
	#pagination_class = PostPageNumberPagination
	filterset_class = ArticleFilter
	#permission_classes = [ArticlePermission,]
	#permission_classes = [permissions.IsAuthenticated,]
