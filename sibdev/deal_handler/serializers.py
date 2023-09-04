from django.core.validators import FileExtensionValidator
from deal_handler.models import User
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    deal_file = serializers.FileField(
        required=True, validators=[FileExtensionValidator(allowed_extensions=["csv"])]
    )

    class Meta:
        fields = ["deal_file"]


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
