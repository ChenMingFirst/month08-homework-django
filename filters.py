from django_filters import rest_framework as filters
from .models import User


class UserFilter(filters.FilterSet):
    class Meta:
        # min_age = filters.NumberFilter(field_name='age',lookup_expr='gte')
        # max_age = filters.NumberFilter(field_name='age',lookup_expr='lte')
        model = User
        fields = {
            'username': ['icontains'],
            'payment': ['gte', 'lte'],
            'age':['gte','lte']
        }