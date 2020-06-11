from rest_framework import serializers
from drfapp.models import Article, AuthorProfile
from django.contrib.auth.models import User


class AuthorProfileSerializers(serializers.ModelSerializer):

	class Meta:
		model  = AuthorProfile

		fields = (
			'first_name',
			'last_name'
			)

	def create(self, validated_data):
		validated_data['user'] = self.context['request'].user
		creaete_user = AuthorProfile.objects.create(**validated_data)
		return creaete_user	

class UserDetailsSerializers(serializers.ModelSerializer):

	class Meta:
		model = User

		fields = [
          'email',
          'first_name',
          'last_name',
          'is_active'
		]



class ArticleSerializers(serializers.ModelSerializer):

	created_by = UserDetailsSerializers(read_only=True)
	class Meta:
		model = Article

		fields = [
		   'id',
           'content',
           'created_date',
           'created_by'

   		]

    
	def create(self, validated_data):
		validated_data['created_by'] = self.context['request'].user
		creaete_user = Article.objects.create(**validated_data)
		return creaete_user	

	def validate(self, validated_data):
		instance = Article(**validated_data)
		instance.clean()
		return validated_data