from rest_framework import serializers
from .seive import perform_analysis
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

# from .serializers import GetUserDocSerializer
from .seive import perform_analysis


class GetUserDocSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    owner = serializers.CharField(required=True)
    init_wt = serializers.CharField(required=True)

    def validate_init_wt(self, value):
        """
        Validate that init_wt is a valid float.
        """
        try:
            float(value)
        except ValueError:
            raise serializers.ValidationError("Initial weight must be a valid number.")
        return value


class GetUserDoc(GenericAPIView):
    serializer_class = GetUserDocSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        file = serializer.validated_data["file"]
        owner = serializer.validated_data["owner"]
        init_wt = serializer.validated_data["init_wt"]

        response = perform_analysis(file, owner, init_wt)
        if response is False:
            return Response(
                {"detail": "File is empty or has invalid data types"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response({"detail": response})
