from django_filters import rest_framework as filters
from .models import Album


class AlbumFilter(filters.FilterSet):
    cost__gte = filters.NumberFilter(field_name="cost", lookup_expr='gte')
    cost__lte = filters.NumberFilter(field_name="cost", lookup_expr='lte')
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = ['cost', 'name']