from rest_framework.permissions import BasePermission


class ArticlePermission(BasePermission):
    def has_permission(self, request, view):
    	return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
    	return obj.created_by == request.user.is_staff

        
			
class AuthorProfilePermission(BasePermission):

	def  has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		return obj.user == request.user.is_authenticated	