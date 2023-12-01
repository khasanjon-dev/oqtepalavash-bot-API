from rest_framework.generics import ListAPIView

from company.models import Region
from company.serializers import RegionModelSerializer


class RegionListAPIView(ListAPIView):
    """
    region lar listi

    ```
    """
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
