from decimal import Decimal

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from deal_handler.models import User, Gem
from deal_handler.serializers import DealSerializer, FileSerializer
from deal_handler.utils import prepare_deals


class DealViewSet(GenericViewSet):
    queryset = User.objects.all().distinct()
    serializer_class = DealSerializer

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.order_by("-spent_money")[:5]

        return self.queryset

    def create(self, request):
        file_serializer = FileSerializer(data=request.FILES)
        file_serializer.is_valid(raise_exception=True)

        try:
            total_deals = prepare_deals(request.FILES.get("deal_file"))
        except Exception as err:
            return Response(
                data={"status": "Error", "desc": f"{err} -  процессе обработки файла произошла ошибка"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        for deal in total_deals:
            username = deal["customer"]
            spent_money = deal["total"]
            gem_name = deal["item"]

            if not Gem.objects.filter(name=gem_name).exists():
                Gem.objects.create(name=gem_name)

            if user := User.objects.filter(username=username).first():
                user.spent_money += Decimal(spent_money)
                user.save()
            else:
                User.objects.create(username=username, spent_money=spent_money)

        # add gems to user

        return Response(data={"status": "OK"}, status=status.HTTP_201_CREATED)

    def list(self, request, pk=None):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
