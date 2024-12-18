# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
	def has_object_permission(self, request, view, obj):
		# Read-only permissions are allowed for any request
		# Permissões somente leitura são permitidas 
		# para qualquer requisição
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the author of a pos
		# As permissões de escrita são permitidas apenas 
		# ao autor de uma postagem
		return obj.author == request.user