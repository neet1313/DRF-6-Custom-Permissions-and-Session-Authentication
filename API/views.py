from rest_framework import viewsets
from API import serializers, models
from rest_framework.authentication import SessionAuthentication
from .custompermissions import CustomPermission
# Create your views here.

# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    #  ------ Session Authentication ------

    # Add Path in urls.py for session Authentication
    authentication_classes = [SessionAuthentication]
    permission_classes = [CustomPermission]
