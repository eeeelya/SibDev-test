from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from deal_handler.models import Deal
from deal_handler.serializers import DealSerializer, FileSerializer
from deal_handler.utils import prepare_deals


class DealViewSet(GenericViewSet):
    queryset = Deal.objects.all().distinct()
    serializer_class = DealSerializer

    def create(self, request):
        file_serializer = FileSerializer(data=request.FILES)
        file_serializer.is_valid(raise_exception=True)

        total_deals = prepare_deals(request.FILES.get("deal_file"))

        Deal.objects.bulk_create([Deal(**deal) for deal in total_deals])

        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, pk=None):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
