from rest_framework.serializers import ModelSerializer

from company.models import Region


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name')
