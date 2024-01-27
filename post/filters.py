import django_filters
from .models import Post

class PostFiltre(django_filters.FilterSet):
    class Meta:
        model=Post
        fields=['objet']